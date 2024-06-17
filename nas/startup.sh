#!/bin/bash
for dir in  "$PWD/pihole" \
            "$PWD/s3" \
            "$PWD/nginx" \
            "$PWD/letsencrypt" \
            "$PWD/postgres" \
            "$PWD/pgadmin" \
            "$PWD/torrent" \

do 
  if [ -d "$dir" ]; then
    echo "Directory $dir exists."
  else
    echo "Directory $dir does not exist. Creating new directory."
    mkdir -p $dir
  fi
done

# check for network connectivity
while true
do
  if ping -c 1 -W 5 google.com 1>/dev/null 2>&1 
  then
    docker container prune --force
    docker compose up -d
    break
  else 
    sleep 5
  fi
done


