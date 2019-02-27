#!/usr/bin/env bash

docker rm -f gongfudou_web

docker rmi -f gongfudou_web

docker build -t gongfudou_web .

docker run -d --name gongfudou_web gongfudou_web