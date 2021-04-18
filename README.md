### micro bp
- this project is a theme for create microservices, using multistaging docker

### DEVELOPMENT

- you need to replace
```python 
    .env.dev_example TO .env.dev
    .env_example TO .env
    .env_prod_db_example TO .env_prod_db
 ``` 

#### BUILD
```python
    docker-compose build
```

#### UP 
```python
    docker-compose up -d
```

#### MIGRATE 
```python
    docker-compose exec api python manage.py migrate 
```

#### CREATE APP 
```python
    docker-compose exec api python manage.py startapp NAME_APP 
```

### PRODUCTION
### BUILD 
```python
    docker-compose -f docker-compose.prod.yml build 
```
### UP 
```python
    docker-compose -f docker-compose.prod.yml up -d 
``` 

the rest of commands below, is a refference, to use in production or development mode, just change 

Markup: > docker-compose -f docker-compose.prod.yml to docker-compose or biceversa
        >> docker-compose -f docker-compose.prod.yml exec api python manage.py migrate 
        >> docker-compose exec api python manage.py migrate

### docker logs show
```python
   docker-compose logs -f 
```

### docker migrate
```python
    docker-compose exec api python manage.py flush --no-input
    docker-compose exec api python manage.py migrate
    or
    docker-compose exec api python manage.py migrate --noinput
```

### docker show data base
```python
    docker-compose exec db psql --username=micro_bp_user --dbname=micro_bp_db
```

### docker inspect
```python
    docker volume inspect micro-bp_postgres_data
```

