#!/bin/bash


add_docker_user(){
    echo "Adding docker user..."
    sudo groupadd docker
    sudo usermod -aG docker $USER
}

start_docker_on_boot(){
    sudo systemctl enable docker.service
    sudo systemctl enable containerd.service
}

add_docker_user
start_docker_on_boot
