# django-project-template-docker

## Requirements

#### System packages
* docker

#### Python packages
* Pip
* docker-compose

##### Install docker

`wget -qO- https://get.docker.com/ | sh`

##### Install docker-compose

`sudo pip install docker-compose`

## Install project

##### 1. Create project:

    django-admin.py startproject --template=https://github.com/abalx/django-project-template-docker/zipball/master --extension py,yml project_name
    
##### 2. Set environment

`cp configs/env.template docker/.env`

`vim docker/.env`
    
##### 3. Run project for development

`docker-compose -f docker/docker-compose.yml up`

That's it. By default the project is available at `0.0.0.0:8000`

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
