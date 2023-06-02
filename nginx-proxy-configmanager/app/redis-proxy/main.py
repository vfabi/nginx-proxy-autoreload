#!/usr/bin/env python3

import os
import time
from lib import ExtDataRedisSentinel, NginxConfigRedis


NGINX_CONFIG_FILE = os.getenv('NGINX_CONFIG_FILE')
REDIS_SENTINEL_ADDRESSES = os.getenv('REDIS_SENTINEL_ADDRESSES')  # Example: "redis-cluster-node-0.redis-cluster-headless.ssai.svc.cluster.local,redis-cluster-node-1.redis-cluster-headless.ssai.svc.cluster.local,redis-cluster-node-2.redis-cluster-headless.ssai.svc.cluster.local"
REDIS_SENTINEL_PORT = int(os.getenv('REDIS_SENTINEL_PORT', 26379))
REDIS_SENTINEL_PASSWORD = os.getenv('REDIS_SENTINEL_PASSWORD')
REDIS_SENTINEL_MASTER_NAME = os.getenv('REDIS_SENTINEL_MASTER_NAME', 'mymaster')
APP_LOOP_TIMEOUT = 3


if __name__ == "__main__":
    while True:
        time.sleep(APP_LOOP_TIMEOUT)
        redis_sentinel = ExtDataRedisSentinel(
            sentinel_addresses = REDIS_SENTINEL_ADDRESSES,
            sentinel_password = REDIS_SENTINEL_PASSWORD,
            sentinel_master_name = REDIS_SENTINEL_MASTER_NAME,
            sentinel_port = REDIS_SENTINEL_PORT
        )
        redis_master_address = redis_sentinel.get_redis_master_address()
        nginx_config = NginxConfigRedis(NGINX_CONFIG_FILE)
        nginx_config.check_config(redis_master_address)
