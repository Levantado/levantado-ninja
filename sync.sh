#!/usr/bin/env bash

rsync -azP ./ MyDO:/home/levantado/dm
ssh MyDO docker-compose -f /home/levantado/dm/docker-compose.yml up -d --build