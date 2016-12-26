# django-project-template

## Requirements
#### System packages
* bash
* python3.4+
* nodejs 6+

#### Python packages
* Pip
* Django 1.10

## Install project
Create project:

    django-admin.py startproject --template=https://github.com/abalx/django-project-template/zipball/master --extension py,.gitignore,scss,docker-compose.yml project_name

Prepare project for development:

    python3 prepare.py

Prepare project for production:

    python3 prepare.py -p
    
## Frontend
#### Description
This project has separate frontend layer. It's in directory `src/frontend`.
There're directories:

* `apps` - static and templates of applications

* `assets` - there're two files - `main.js` and `main.scss`. They should import other static files (import manually)

* `build` - compiled static by gulp and webpack

* `node_modules` - npm applications

* `vendor` - bower applications

`media` and `staticroot` will be also here.

#### Frontend commands
Before work with frontend run the command (being in `src/frontend`):
    
    npm install
    
Work with static (being in `src/frontend`):

    gulp

Compile static for production (being in `src/frontend`). Do it on production server:

    gulp production

Creating new frontend application directory:

    python3 src/manage.py startfrontendapp <APPLICATION_NAME>

Will be created new frontend app directory:

    src/
        frontend/
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
