#!/bin/bash

echo ----Updating Packages------
sudo apt-get update -y

echo ----Installing Python-----
sudo apt-get install software-properties-common -y

echo -----Moving to App Folder-----
cd ../vagrant/app
pwd


# echo -----Starting game-----
# python3 game.py

