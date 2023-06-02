#!/usr/bin/env python3

import re
import os
from redis.sentinel import Sentinel, MasterNotFoundError


class ExtDataRedisSentinel:

    def __init__(self, sentinel_addresses, sentinel_password, sentinel_master_name, sentinel_port=26379):
        self.sentinel_addresses = sentinel_addresses.split(',')
        self.sentinel_port = sentinel_port
        self.sentinel_password = sentinel_password
        self.sentinel_master_name = sentinel_master_name

    def get_redis_master_address(self):
        for sentinel_address in self.sentinel_addresses:
            try:
                sentinel = Sentinel(
                    [(sentinel_address, self.sentinel_port)],
                    socket_timeout=0.1,
                    sentinel_kwargs={'password': self.sentinel_password}
                )
                host, port = sentinel.discover_master(self.sentinel_master_name)
                break
            except MasterNotFoundError:
                pass
        return host


class NginxConfigRedis:

    NGINX_CONFIG_TEMPLATE_REDIS = """stream {
    server {
        listen 6379;
        proxy_pass REDIS_MASTER_ADDRESS:6379;
        proxy_socket_keepalive on;
        proxy_timeout 60m;
        proxy_connect_timeout 10s;
        # proxy_protocol off;
    }
}"""

    def __init__(self, nginx_config_file):
        self.nginx_config_file = nginx_config_file
        self.nginx_config_update = True

    def check_config(self, redis_master_address):
        if not os.path.isfile(self.nginx_config_file):
            print(f'Nginx config file is not found. Creating {self.nginx_config_file} file.')
            nginx_config_content = self.NGINX_CONFIG_TEMPLATE_REDIS.replace('REDIS_MASTER_ADDRESS', redis_master_address)
            with open(self.nginx_config_file, 'w') as wfile:
                wfile.write(nginx_config_content)
        else:
            with open(self.nginx_config_file, 'r') as rfile:
                for line in rfile:
                    match_redis_server_string = re.match(f'proxy_pass {redis_master_address}:6379;$', line.strip())
                    if match_redis_server_string:
                        # current_redis_server_string = match_redis_server_string.group(0)
                        self.nginx_config_update = False
                        break
                if self.nginx_config_update:
                    print(f'Got new Redis master address - {redis_master_address}.')
                    self.replace_string(redis_master_address)

    def replace_string(self, redis_master_address):
        nginx_config_content = self.NGINX_CONFIG_TEMPLATE_REDIS.replace('REDIS_MASTER_ADDRESS', redis_master_address)
        with open(self.nginx_config_file, 'w') as wfile:
            wfile.write(nginx_config_content)
        print(f'Updated Nginx config file. New Redis master address is {redis_master_address}.')
