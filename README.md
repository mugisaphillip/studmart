# studmart
Studmart is a web application that allows students and young people to create, manage, and grow their businesses. The platform offers an online presence and advertisement for businesses across different institutions, hence breaking the barrier of distance. With countless products, a user-friendly interface, and quick search and filtering tools, users can  find products of their interest in a split second.

Go ahead and have a look: [StudMart](http://studmart.mugisa.tech/). Checkout the inspiration and background of StudMart: [Redefining student businesses in Africa.](https://medium.com/@phillipmugisa4/studmart-redefining-student-businesses-f6c37a897ce8)

## Authors and contributors
- [Mugisa Phillip](https://github.com/mugisaphillip)

## Technologies Used
- Python (Django): The core of the platform is built using Django, a high-level Python web framework.
- Vanilla Javascript


## Features
- User authentication
- Seller dashboard: Our seller dashboard offers an easy way of managing all your business details.
- multiple business creation: A user is able to manage as many businesses across different institution on in platform.
- Product/service Search and Filtering

## Project Set Up manually
```bash
    git clone https://github.com/mugisaphillip/studmart.git
    cd studmart
    sudo apt update
    sudo apt install python3 -y
    sudo apt install python3.8-venv -y
```

```python
    python3 -m venv venv
```

```bash
    source ./venv/bin/activate
    cd src
```

```python
    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata ./.db.bak.json
    python manage.py runserver 0.0.0.0:9090
```

# Project Set using bash script
```bash
    git clone https://github.com/mugisaphillip/studmart.git
    cd studmart
    chmod +x ./prod/setup.sh
    ./prod/setup.sh
```