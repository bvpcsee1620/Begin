# erp-server [![Build Status](https://travis-ci.com/Aniket965/erp-server.svg?token=D3fcTy46y2xL1GvHa3f6&branch=master)](https://travis-ci.com/Aniket965/erp-server)
This is api server in flask for faculty portal.


- Use following Command to start:

```sh
$ python manage.py db init
$ ./update.sh
```

**Add Trigger For Real Time Notification**
> **Note** - you have to select database first in psql session

> first create function
```sh
test=>\i 'pathtocreate_function.sql'
```
> then create trigger
```sh
test=>\i 'pathtocreate_triggers.sql'
```

> **Note - if you change models.py it is required to migrate**

- To update changes:

```sh
$ ./update.sh
```


- Delete **ALL TABLES** in a Database:

```
DB_NAME=# DROP SCHEMA public CASCADE;
DB_NAME=# CREATE SCHEMA public;
DB_NAME=# GRANT ALL ON SCHEMA public TO postgres;
DB_NAME=# GRANT ALL ON SCHEMA public TO public;
```

## docker development

```sh
docker-compose build
docker-compose up -d
docker-compose exec app python manage.py recreate_db
```

```sh
docker pull aniket965/erp-portal
```
