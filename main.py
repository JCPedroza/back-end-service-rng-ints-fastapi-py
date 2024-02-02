from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from random import randrange

MAX_SIZE = 100
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_root():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Root</title>
        </head>
        <body>
            <p>Docs at /docs</p>
        </body>
    </html>
    """


@app.get("/rng/ints/{size}")
async def get_rng_ints_SIZE(size: int, start: int = -10, end: int = 11):
    """
    Get a list of random integers.

    - **size (path)**: Number of random integers that the list will contain.
    - **start (query)**: Minimum value of the random integers (inclusive).
    - **end (query)**: Maximum value of the random integers (exclusive).
    """
    if size < 0 or size > MAX_SIZE:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            f"size needs to be in the range [0, 100] (size:{size})",
        )

    if end < start:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            f"start can't be greater than end (start:{start} end:{end})",
        )

    return {"ints": [randrange(start, end) for _ in range(size)]}
