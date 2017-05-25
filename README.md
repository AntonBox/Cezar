# Project Django Shop

## Prerequisites

- Python 3.5
- pip
- virtualenv (or pew)(I`m using pew https://github.com/berdario/pew) 
- PostgreSQL

## Installation

### 1. Create virtualenv

#### If you are using pew:

```
    pew new -p python3.5 cezar
    pew workon cezar
```


### 2. Install dependencies

#### Install neccessary *-dev packages::

```
    sudo apt-get install python3-dev
```

#### Pillow package dependencies:

```
    sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

#### Django dependencies:

```
    pip install -r requirements-dev.txt
```


### 3. Database:

#### Install PostgreSQL.

#### Create database:

```
    sudo -i -u postgres
    createuser cezar -P
    createdb cezar -O cezar
    exit
```

#### Migrate database:

```
    python manage.py migrate
```


### 4. Run project:

```
    make run
```
