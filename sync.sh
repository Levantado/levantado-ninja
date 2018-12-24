#!/usr/bin/env bash

rsync -azP ./ MyDO:/home/levantado/dm
#ssh MyDO docker-compose -f /home/levantado/dm/docker-compose.yml up -d --build
rsync -azP --delete \
    --include .git --exclude-from="$(git -C . ls-files \
        --exclude-standard -oi --directory >.git/ignores.tmp && \
        echo .git/ignores.tmp)" . MyDO:/home/levantado/dm2
