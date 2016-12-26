# django-project-template

## Requirements

#### System packages
* docker

#### Python packages
* Pip
* docker-compose

##### Install docker

`wget -qO- https://get.docker.com/ | sh`

##### Install docker-composee

`sudo pip install docker-compose`

## Install project

##### Create project:

    django-admin.py startproject --template=https://github.com/abalx/django-project-template-docker/zipball/master --extension py,docker-compose.yml project_name
    
##### Run project for development

`docker-compose -f docker/docker-compose.yml up`

##### Run project for production

`docker-compose -f docker/docker-compose.yml -f docker/docker-compose.prod.yml up`

## Client
#### Description

This project has separate frontend layer. It's in directory `client`.
There're directories:

* `apps` - static and templates of applications

* `assets` - there're two files - `main.js` and `main.scss`. They should import other static files (import manually)

* `build` - compiled static by gulp and webpack

* `node_modules` - npm applications

* `vendor` - bower applications

`media_root` and `static_root` will be also here.

#### Client commands

Create a new client application:

    docker exec -it <PROJECT_NAME>_server python server/manage.py startclientapp <APPLICATION_NAME>

Will be created a new client app:

    client/
        apps/
            APPLICATION_NAME/
                static/
                    APPLICATION_NAME/
                        images/
                        js/
                            APPLICATION_NAME.js
                        styles/
                            APPLICATION_NAME.scss
                templates/
                    APPLICATION_NAME/
