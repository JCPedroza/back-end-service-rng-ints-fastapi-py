from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from random import randrange

START = -99
STOP = 100
MIN_SIZE = 1
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
async def get_rng_ints_SIZE(size: int, start: int = START, stop: int = STOP):
    """
    Get a list of random integers.

    - **size (path)**: Number of random integers that the list will contain.
    - **start (query)**: Minimum value of the random integers (inclusive).
    - **stop (query)**: Maximum value of the random integers (exclusive).
    """
    if size < MIN_SIZE or size > MAX_SIZE:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            f"size must be in the range [{MIN_SIZE}, {MAX_SIZE}] (size:{size})",
        )

    if stop <= start:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            f"stop must be greater than start (start:{start} stop:{stop})",
        )

    return {"ints": [randrange(start, stop) for _ in range(size)]}
