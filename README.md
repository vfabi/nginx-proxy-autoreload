# nginx-proxy-autoreload

Nginx based proxy with autoreload on configuration changes.  
Сonsists of two components:  
- Nginx with autoreload config feature  (nginx-proxy-autoreload)
- Nginx config dynamic provisioning application (nginx-proxy-configmanager)

## Features

- Nginx as a proxy behind main application
- Reload Nginx on its config changes
- Nginx config dynamic provisioning

Nginx dynamic configuration implementations:
- redis-proxy - Redis proxy configuration for Nginx. Nginx config provisiong application get Redis master address from Redis Sentinel and updates Nginx config.

## Technology stack

- Nginx
- Python for Nginx config provision app 

## Requirements and dependencies

## Configuration

## Deployment

For the Kubernetes cluster please apply configuration from `deployment/kubernetes/<PROXY-IMPLEMENTATION>/*.yaml`

## Usage

## Docker

[![Generic badge](https://img.shields.io/badge/hub.docker.com-vfabi/nginx_proxy_autoreload-<>.svg)](https://hub.docker.com/repository/docker/vfabi/nginx-proxy-autoreload)  
[![Generic badge](https://img.shields.io/badge/hub.docker.com-vfabi/nginx_proxy_configmanager-<>.svg)](https://hub.docker.com/repository/docker/vfabi/nginx-proxy-configmanager)

## Build

## Contributing

Please refer to each project's style and contribution guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

NOTE: Be sure to merge the latest from "upstream" before making a pull request!

## License

Apache 2.0