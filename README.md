# studmart

# Project Set Up manually
`bash
    git clone https://github.com/mugisaphillip/studmart.git
    cd studmart
    sudo apt update
    sudo apt install python3 -y
    sudo apt install python3.8-venv -y
`

`python
    python3 -m venv venv
`

`bash
    source ./venv/bin/activate
    cd src
`

`python
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata ./.db.bak.json
    python manage.py runserver 0.0.0.0:9090
`

# Project Set using bash script