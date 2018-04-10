#!/usr/bin/env bash

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://uttarakulkarni@bitbucket.org/281_project/water_watch_service.git'

PROJECT_BASE_PATH='/usr/local/apps'
VIRTUALENV_BASE_PATH='/usr/local/virtualenvs'

# Set Ubuntu Language
locale-gen en_GB.UTF-8

# Install Python, SQLite and pip
apt-get update
apt-get install -y python3-dev postgres sqlite python-pip supervisor nginx git

# Upgrade pip to the latest version.
pip install --upgrade pip
pip install virtualenv

mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH/water_watch_service

mkdir -p $VIRTUALENV_BASE_PATH
virtualenv  $VIRTUALENV_BASE_PATH/water_watch_api

source $VIRTUALENV_BASE_PATH/water_watch_api/bin/activate
pip install -r $PROJECT_BASE_PATH/water_watch_service/requirements.txt

# Run migrations
cd $PROJECT_BASE_PATH/water_watch_service/src

# Setup Supervisor to run our uwsgi process.
cp $PROJECT_BASE_PATH/water_watch_service/deploy/supervisor.conf /etc/supervisor/conf.d/water_watch_api.conf
supervisorctl reread
supervisorctl update
supervisorctl restart water_watch_api

# Setup nginx to make our application accessible.
cp $PROJECT_BASE_PATH/water_watch_service/deploy/nginx_water.conf /etc/nginx/sites-available/water_watch_api.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/water_watch_api.conf /etc/nginx/sites-enabled/water_watch_api.conf
systemctl restart nginx.service

echo "DONE! :)"
