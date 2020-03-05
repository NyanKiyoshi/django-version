<div align='center'>
  <h1>django-version</h1>
  <p>
    A middleware retrieving a project version from settings and returning it in the response headers.<br/>
    Appends <code>X-Project-Version: a.b.c</code> to every response.
  </p>
  <p>
    <a href='https://travis-ci.org/NyanKiyoshi/django-version/'>
      <img src='https://travis-ci.org/NyanKiyoshi/django-version.svg?branch=master' alt='Requirement Status' />
    </a>
    <a href='https://pypi.python.org/pypi/django-version'>
      <img src='https://img.shields.io/pypi/v/django-version.svg' alt='Version' />
    </a>
    <a href='https://pypi.python.org/pypi/django-version'>
      <img src='https://img.shields.io/pypi/pyversions/django-version.svg' alt='Supported versions' />
    </a>
    <a href='https://pypi.python.org/pypi/django-version'>
      <img src='https://img.shields.io/pypi/implementation/django-version.svg' alt='Supported implementations' />
    </a>
  </p>
</div>

## Installation
```shell script
$ pip install django-version
```

## Usage
1. Append `django_version` to `INSTALLED_APPS`
1. Append `django_version.VersionMiddleware` to `MIDDLEWARE`
1. Set your project version into the setting key `PROJECT_VERSION` as a string
