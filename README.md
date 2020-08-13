# docker-hostname

## これはなに?

Getリクエストを受け取ると,マシンのホスト名を返します.

ロードバランサのテストに用いることを想定しています.

## ビルド方法

    docker build --tag docker-hostname .    

## 使い方

    docker run -d --rm -p 80:80 docker-hostname:latest   