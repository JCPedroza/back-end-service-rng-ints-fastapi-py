# Back-End Practice: Random Integers Service with Python and FastAPI

This is an exercise to showcase the basic routing and request-response features
of the FastAPI framework.

## Task

* Create a service at the `/rng/ints/:size` endpoint that will generate a list
of random integer numbers.

* The size of the list is specified as path parameter, and must be an integer
greater than zero but no larger than 100.

* The minimum and maximum values of the randomly generated numbers are
specified as query parameters, and must be integers where the minimum is never
greater than the maximum.

* Apply type validation and constraint validation. Respond with a 400-family
code to handle invalid values.

## Installation

You need both `Python` and `pip`. Then you can use pip to install the
dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Once everything is installed, you can run the server using:

```bash
uvicorn main:app
```
