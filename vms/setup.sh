#!/bin/bash

DOCKER_USER=$1
DOCKER_PASSWORD=$2

echo "DOCKER_USER=$DOCKER_USER"
echo "DOCKER_PASSWORD=$DOCKER_PASSWORD"

setup_docker_apt() {
    # Add Docker's official GPG key:
    echo "Running docker apt setup..."
    sudo apt-get update
    sudo apt-get install ca-certificates curl
    sudo install -m 0755 -d /etc/apt/keyrings
    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
    sudo chmod a+r /etc/apt/keyrings/docker.asc

    # Add the repository to Apt sources:
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
    $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
    sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
}

# Install docker packages
install_docker_packages(){
    echo "Installing docker packages..."
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
}

login_docker(){
    echo "Logging into Docker..."
    docker login ghcr.io -u $DOCKER_USER -p $DOCKER_PASSWORD
}


setup_docker_apt && install_docker_packages && sudo docker run hello-world && login_docker
