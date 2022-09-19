# TMS diploma project "Secret santa"

Author: Dima Ulasovets
Teacher: Hleb Serafimovich

About project:
Secret Santa is a graduation project from the TMS school. In this project, the logic of the secret santa game was implemented using technologies such as: Python, DRF, Celery, PostgreSQL, Redis, JWT, RestAPI

## Usage with Docker

go to project folder

```bash
cd secret_santa/secret_santa
```

run docker-compose.yaml to build oure project into docker conteiner
```bash
docker-compose up
```

open terminal and dive into docker container
```bash
docker exec -it secret_santa_app_1 bash
```

start migrations
```bash
python manage.py migrate
```

create superuser
```bash
python manage.py createsuperuser
```

check oure project in brouser
```bash
http://127.0.0.1:8000/
```

## Usage with GitHub

clone project from github
```bash
git clone git@github.com:DimaUlasovets/secret_santa.git
```

create environment with poetry
```bash
poetry shell
```

create environment with python virtualenv
 ```bash
python3 -m venv venv
```

activate virtualenv
 ```bash
source venv/bin/activate
```

install package
 ```bash
pip3 install -r requirements.txt
```

Create PostgreSQL DB, check .env file
Create Redis DB, check .env file

start migrations
```bash
python manage.py migrate
```

Start celery worker
```bash
celery -A secret_santa worker -l INFO
```

Start project
```bash
python manage.py runserver
```

check oure project in brouser
```bash
http://127.0.0.1:8000/
```
