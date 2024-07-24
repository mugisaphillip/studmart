# studmart

# Project Set Up
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
    pip install -r requirements.txt
    cd src
`

`python
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata ./.db.bak.json
`