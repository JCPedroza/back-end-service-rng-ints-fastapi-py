# Back-End Practice: Random Integers Service with Python and FastAPI

This is an exercise to showcase:

* The basic routing and request-response features of the [FastAPI][0]
framework.

* [Python][1] as a back-end language.

## Task

* Create a service at the `/rng/ints/:size` endpoint that will generate a list
of random integer numbers, and serve it as JSON.

* The size of the list is specified as path parameter, and must be an integer
greater than zero but no larger than 100.

* The minimum and maximum values of the randomly generated numbers are
specified as required query parameters, and must be integers where the maximum
value is always greater than the minimum value.

* Apply type validation and constraint validation. Respond with a 400-family
code to handle invalid values.

* Root should display an html message that directs the user to either the API
documentation or the random integers service.

## Example URL - Response

### Valid Values

```text
/rng/ints/5?start=-10&stop=11
```

```text
HTTP/1.1 200 OK
content-length: 21
content-type: application/json
date: Fri, 09 Feb 2024 04:19:12 GMT
server: uvicorn
```

```json
{
    "ints": [
        9,
        3,
        7,
        -1,
        8
    ]
}
```

### Invalid Value Range

```text
/rng/ints/5?start=7&stop=7
```

```text
HTTP/1.1 422 Unprocessable Entity
content-length: 55
content-type: application/json
date: Fri, 09 Feb 2024 04:30:42 GMT
server: uvicorn
```

```json
{
    "detail": "(stop=7) must be greater than (start=7)"
}
```

### Invalid Size

```text
/rng/ints/0?start=1&stop=11
```

```text
content-length: 203
content-type: application/json
date: Fri, 09 Feb 2024 04:32:51 GMT
server: uvicorn
```

```json
{
    "detail": [
        {
            "ctx": {
                "ge": 1
            },
            "input": "0",
            "loc": [
                "path",
                "size"
            ],
            "msg": "Input should be greater than or equal to 1",
            "type": "greater_than_equal",
            "url": "https://errors.pydantic.dev/2.6/v/greater_than_equal"
        }
    ]
}
```

### Missing Required Query Parameters

```text
localhost:8000/rng/ints/10
```

```text
HTTP/1.1 422 Unprocessable Entity
content-length: 269
content-type: application/json
date: Fri, 09 Feb 2024 04:36:28 GMT
server: uvicorn
```

```json
{
    "detail": [
        {
            "input": null,
            "loc": [
                "query",
                "start"
            ],
            "msg": "Field required",
            "type": "missing",
            "url": "https://errors.pydantic.dev/2.6/v/missing"
        },
        {
            "input": null,
            "loc": [
                "query",
                "stop"
            ],
            "msg": "Field required",
            "type": "missing",
            "url": "https://errors.pydantic.dev/2.6/v/missing"
        }
    ]
}
```

## Installation

You need both [Python][2] and [pip][3]. Then you can use pip to install the
dependencies. The only core dependencies needed are `fastapi` and `uvicorn`:

```bash
python -m pip install fastapi uvicorn
```

Or you can install directly from the requirements file, which will also install
type checkers and linters if you want them:

```bash
python -m pip install -r requirements.txt
```

## Usage

Once everything is installed, you can run the server using:

```bash
uvicorn main:app
```

## Notes

In FastAPI:
 * HTTP verbs aka HTTP methods are known as *operations*.
 * Handlers are known as *path operation functions*.
 * Variable parts of a path are known as *path parameters*.
 * Query strings are known as *query parameters*.

Decorators are used to link together *operation*, *path*, and *path
operation function*.

Routing uses the general pattern:

```text
@<FastAPI instance>.<operation>(<path>)
<path operation function>
```

The whole line `@<FastAPI instance>.<operation>(<path>)` is known as *path
operation decorator*, and decorates the *path operation function*, which
is assigned to that specific *operation* and *path*.

*Path parameters* are declared in the *path* between `{}` and also declared
as parameters to the *path operation function*.

*Query parameters* are only declared as parameters to the *path operation
function*, and the ones without a default value assigned to them will be
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

When handling bad input, it is preferable to raise an `HTTPException` than
setting the status yourself and explicitly creating a `Response` instance. This
way the `HTTPException` is documented in `OpenAPI`.

---

[0]: https://fastapi.tiangolo.com/
[1]: https://www.python.org/
[2]: https://www.python.org/downloads/
[3]: https://pip.pypa.io/en/stable/installation/
