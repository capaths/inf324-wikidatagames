#!/bin/bash

function clean() {
    echo "Stopping and removing container $1"
    docker rm -f $1
}

function run() {
    echo "Running container $1 at port $3"
    docker run -p "$3:5000" -d --name $2 $1
}

clean access-service
clean chat-service
clean match-service
clean player-service
clean ticket-service

. ports.cfg
run capaths/games-access access-service  $access
run capaths/games-chat chat-service  $chat
run capaths/games-match match-service  $match
run capaths/games-player player-service  $player
run capaths/games-ticket ticket-service  $ticket
