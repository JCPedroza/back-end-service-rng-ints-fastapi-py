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

* Root should display an html message that directs user either to the API
documentation or to the random integers service.

## Installation

You need both `Python` and `pip`. Then you can use pip to install the
dependencies:

```bash
pip install fastapi uvicorn
```

Or you can install directly from the requirements file:

```bash
pip install -r requirements.txt
```

## Usage

Once everything is installed, you can run the server using:

```bash
uvicorn main:app
```

## Notes

Remember that in FastAPI:
 * HTTP verbs aka HTTP methods are known as *operations*.
 * Handlers are known as *path operation functions*.
 * Variable parts of a path are known as *path parameters*.
 * Query strings are known as *query parameters*.

Routing in FastAPI uses the general pattern:

```text
@<FastAPI instance>.<operation>(<path>)
<path operation function>
```

Path parameters are declared in the path string between `{}` and also declared
as parameters to the path operation function.

Query parameters are only declared as parameters to the path operation
function, and the ones without a default value assigned to them will be
declared as required.

Example:

```Python
@app.get("/somepath/{num}")
def get_user_idn(num: int, qry1: bool, qry2: str = "default"):
    return {
        "path parameter": num,
        "query parameter 1": qry1,
        "query parameter 2": qry2
    }
```

When handling bad input, it is preferable to raise an HTTPException than
setting the status yourself and explicitly creating a Response instance. This
way the HTTPException is documented in OpenAPI.

## Useful Imports

```Python
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
```
