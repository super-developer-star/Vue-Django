# Vue + Django Rest Framework

## Prerequisites

Before getting started you should have the following installed and running:

- [X] Yarn - [instructions](https://yarnpkg.com/en/docs/install#mac-stable)
- [X] Vue Cli 3 - [instructions](https://cli.vuejs.org/guide/installation.html)
- [X] Python 3
- [X] Pipenv

## Setup Template

Setup
```
$ yarn install
$ pipenv install --dev
$ pipenv shell
$ python manage.py migrate
```

## Running Development Servers
It is django backend server
```
$ python manage.py runserver
```

From another tab in the same directory:
It is vue frontend server
```
$ yarn serve
```

The Vuejs application will be served from `localhost:8080` and the Django Api
and static files will be served from `localhost:8000`.

The dual dev server setup allows you to take advantage of
webpack's development server with hot module replacement.
Proxy config in `vue.config.js` is used to route the requests
back to django's Api on port 8000.

If you would rather run a single dev server, you can run Django's
development server only on `:8000`, but you have to build build the Vue app first
and the page will not reload on changes.

```
$ yarn build
$ python manage.py runserver
```


## Deploy

* Set `ALLOWED_HOSTS` on `backend.settings.prod.py`

### Heroku Server

```
$ pip freeze > requirements.txt
$ heroku apps:create vue-django
$ heroku git:remote --app vue-django
$ heroku buildpacks:add --index 1 heroku/nodejs
$ heroku buildpacks:add --index 2 heroku/python
$ heroku addons:create heroku-postgresql:hobby-dev
$ heroku config:set DJANGO_SETTINGS_MODULE=backend.settings.prod

$ git push heroku master
```

Heroku's nodejs buidlpack will handle install for all the dependencies from the `packages.json` file.
It will then trigger the `postinstall` command which calls `yarn build`.
This will create the bundled `dist` folder which will be served by whitenoise.

The python buildpack will detect the `pipfile` and install all the python dependencies.

The `Procfile` will run Django migrations and then launch Django'S app using gunicorn, as recommended by heroku.
