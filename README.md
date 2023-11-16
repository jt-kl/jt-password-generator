# jt-password-generator

![tests](https://github.com/jt-kl/jt-password-generator/actions/workflows/hosted_test.yml/badge.svg)
![tests](https://github.com/jt-kl/jt-password-generator/actions/workflows/premise_test.yml/badge.svg)
![build](https://github.com/jt-kl/jt-password-generator/actions/workflows/premise_build.yml/badge.svg)
![coverage](./tests/coverage.svg)

## Getting Started

### Development

```shell
#!/bin/bash
$ cd jt_password_generator
$ python3 -m venv .env
$ source .env/bin/activate
$ python3 -m pip install --upgrade pip
$ pip3 install wheel --no-cache-dir
$ pip3 install -r requirements-dev.txt --no-cache-dir
$ pip3 install redist/* # If applicable
$ pip3 install -e . # Install 'src' as local library

```

## Testing

Execute unit test suite

```shell
#!/bin/bash
$ clear; tox # Scripted multi version tests

```

## Build & Distribute

Create a redistributable wheel file

```shell
#!/bin/bash
# Build the wheel file and on completion, distribute the wheel file located in
# the "dist" directory. The "build" and "dist" directory can be safely removed

$ python3 scripts/upgrade.py <options> # Updates package version number
$ bash scripts/build.sh

```
