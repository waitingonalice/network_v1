#!/bin/bash 

# Install docker desktop
sudo apt-get update
sudo apt-get install ./docker-desktop.deb

systemctl --user start docker-desktop
systemctl --user enable docker-desktop