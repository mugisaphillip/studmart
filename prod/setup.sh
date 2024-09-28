#usr/bin/env bash

# install python and nginx
sudo apt update
sudo apt install python3 -y
sudo apt install nginx -y

# create virtual environment
sudo apt install python3.8-venv -y    
python3 -m venv venv
source ./venv/bin/activate
cd src

# install dependences and run migrations
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate

# load default test data in to db
python manage.py loaddata ./.db.bak.json

# set up nginx
sudo mv ../prod/studmart /etc/nginx/sites-available/studmart
sudo ln -s /etc/nginx/sites-available/studmart /etc/nginx/sites-enabled/studmart
sudo systemctl restart nginx

# set gunicorn
sudo mv ../prod/gunicorn.service /etc/systemd/system/gunicorn.service
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl daemon-reload

# # run application
# python manage.py runserver 0.0.0.0:9090
