# jt-password-generator

## Getting Started

```shell
#!/bin/bash
$ cd jt_password_generator
$ python3 -m venv .env
$ source .env/bin/activate
$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements-dev.txt --no-cache-dir
$ pip3 install redist/* # If applicable
$ pip3 install -e . # Install 'src' as local library
```

### Unit Testing

```shell
$ clear; tox # Scripted multi version tests

$ clear; pytest --cov-report=term-missing --cov=jt_password_manager -vvv -s # With Coverage Report - MANUAL
$ clear; pytest --no-cov -vvv -s # Without Coverage Report (DEBUG Mode) - MANUAL
```

### Linting

```Shell
$ clear; ruff . # Standard checks respecting configs from [pyproject.tool.ruff]
$ clear; ruff check --select F401, E711 # Specific compliance checks for F401 and E711
```

### Type Checking

```shell
$ clear; mypy ./src
```

## Build & Distribute

Create a redistributable wheel file

```shell
#!/bin/bash
$ cd jt_password_generator
$ python3 -m venv .env
$ source .env/bin/activate
$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements-dev.txt --no-cache-dir
$ pip3 install redist/* # If applicable
$ pip3 install -e . # Install 'src' as local library

# Build the wheel file and on completion, distribute the wheel file located in
# the "dist" directory. The "build" and "dist" directory can be safely removed

$ python3 upgrade.py <options>
$ bash build.sh
```
