# django-version

A middleware retrieving a project version from settings and returning it in the response headers.
It will append `X-Project-Version: <a value>` to every response.

## Installation
```shell script
$ pip install django-version
```

## Usage
1. Append `django_version` to `INSTALLED_APPS`
1. Append `django_version.VersionMiddleware` to `MIDDLEWARE`
1. Set your project version inside to the setting key `PROJECT_VERSION`
