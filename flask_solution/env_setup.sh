#!/bin/bash

# This script is for the Debian machine
sudo apt update
sudo apt install python3 python3-venv

# Setting-up the virtual-env
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
