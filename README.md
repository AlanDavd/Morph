# Morph

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://pypi.org/project/black/)
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/pydanny/cookiecutter-django/)

Morph is an image library built to showcase my skills for the Shopify Backend Developer Intern Challenge.

This is what the project can do:

**User**:

It allows you to:

- Sign up
- Log in
- Log out

**Images**:

You can

- Upload one image
- Bulk upload images
- Delete one image
- Bulk delete images

## Run Project

Install and run Morph with Docker

Clone the project

```bash
$ git clone https://github.com/AlanDavd/Morph.git
```

Go to the project directory

```bash
$ cd morph
```

Install dependencies and run the stack

```bash
$ docker-compose -f local.yml build
$ docker-compose -f local.yml up
```


## Util Commands

To run tests, run the following command:

```bash
$ docker-compose -f local.yml run --rm django pytest
```

To run black, run the following command:

```bash
$ docker-compose -f local.yml run --rm django black morph
```

To run flake8, run the following command:

```bash
$ docker-compose -f local.yml run --rm django flake8 morph
```

To run migrations, run the following command:

```bash
$ docker-compose -f local.yml run --rm django python manage.py makemigrations
$ docker-compose -f local.yml run --rm django python manage.py migrate
```

To enable the debugger, run the following commands:

```bash
$ docker ps
$ docker rm -f <django-process-id>
```

And in another session:

```bash
$ docker-compose -f local.yml run --rm --service-ports django
```

## License

[GPLv3](./LICENSE)


## Author

- alandavidrl11@gmail.com
