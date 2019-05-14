#!/usr/bin/env bash

# Install Supervisor
sudo apt-get install -y supervisor

# Make run_production executable
sudo chmod u+x boot.sh

. pyenv/bin/activate
# Install production requirements
sudo pip3 install -r requirements.txt
# Migrate database to newest
env FLASK_CONFIG="production" sudo -E python3 manage.py db upgrade

# Start supervisor service
sudo supervisorctl reread
sudo service supervisor restart