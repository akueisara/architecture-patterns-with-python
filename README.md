# Aarchitecture Pattens with Python

Follow through the exercises in the book *Aarchitecture Pattens with Python by Harry Percival; Bob Gregory*



## Requirements

* docker with docker-compose
* for chapters 1 and 2, and optionally for the rest: a local python3.7 virtualenv



## Building the containers

_(this is only required from chapter 3 onwards)_

```sh
make build
make up
# or
make all # builds, brings containers up, runs tests
```



## Running the tests

```sh
make test
# or, to run individual test types
make unit
make integration
make e2e
# or, if you have a local virtualenv
make up
pytest tests/unit
pytest tests/integration
pytest tests/e2e


## Makefile

There are more useful commands in the makefile, have a look and try them out.


```

