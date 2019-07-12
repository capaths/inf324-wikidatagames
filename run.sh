#!/bin/bash

function clean() {
    echo "Stopping and removing container $1"
    docker rm -f $1
}

function run() {
    echo "Running container $1 at port $3"
    docker run -p "$3:5000" -d --name $2 $1
}

. ./ports.cfg

Services=("access" "chat" "match" "player" "ticket")
Ports=("$access" "$chat" "$match" "$player" "$ticket")

for i in "${!Services[@]}"; do 
    service="${Services[$i]}"
    port="${Ports[$i]}"
    
    clean "$service-service"
    run "capaths/games-$service" "$service-service"  "${Ports[$i]}"
done
