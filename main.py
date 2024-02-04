from fastapi import FastAPI, HTTPException, Path, status
from fastapi.responses import HTMLResponse

from typing import Annotated
from random import randrange

START = -99
STOP = 100
MIN_SIZE = 1
MAX_SIZE = 100
DOCS_PATH = "/docs"
REDOCS_PATH = "/redocs"

app = FastAPI(docs_url=DOCS_PATH, redoc_url=REDOCS_PATH)


@app.get("/", response_class=HTMLResponse)
async def get_root():
    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Root</title>
        </head>
        <body>
            <p>Docs at <ul>
                <li><a href="{DOCS_PATH}">{DOCS_PATH}<a></li>
                <li><a href="{REDOCS_PATH}">{REDOCS_PATH}<a></li>
            </ul></p>
        </body>
    </html>
    """


@app.get("/rng/ints/{size}")
async def get_rng_ints_SIZE(
    size: Annotated[int, Path(ge=MIN_SIZE, le=MAX_SIZE)],
    start: int = START,
    stop: int = STOP,
):
    """
    Get a list of random integers.
    - **size (path)**: Number of random integers that the list will contain.
    - **start (query)**: Minimum value of the random integers (inclusive).
    - **stop (query)**: Maximum value of the random integers (exclusive).
    """
    if stop <= start:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            f"stop must be greater than start (start:{start} stop:{stop})",
        )

    return {"ints": [randrange(start, stop) for _ in range(size)]}
