# docker-hostname

[![Docker Pulls](https://img.shields.io/docker/pulls/tsu001r/docker-hostname.svg)](https://hub.docker.com/r/tsu001r/docker-hostname/)
[![Docker Automated build](https://img.shields.io/docker/automated/tsu001r/docker-hostname.svg)](https://hub.docker.com/r/tsu001r/docker-hostname/)

## what is this? (これはなに?)

When a Get request is received, returns the hostname of the machine.   
It is assumed to be used for load balancer testing.

Getリクエストを受け取ると,マシンのホスト名を返します.  
ロードバランサのテストに用いることを想定しています.

## how to build (ビルド方法)

    docker build --tag docker-hostname .    

## how to use (使い方)

    docker run -d --rm -p 80:80 docker-hostname:latest   