#!/bin/bash

SRC_PATH="src/"

function build_service() {
    serv_path="$SRC_PATH/$(echo $1 | sed 's/\([a-z]*\)/\u\1Service\//g')"
    docker build -t "capaths/games-$1" $serv_path
}

Services=("access" "chat" "match" "player" "ticket")

for service in "${Services[@]}"; do
    build_service $service
done
