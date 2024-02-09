from typing import Annotated
from random import randrange
from fastapi import FastAPI, HTTPException, Path, Query, status
from fastapi.responses import HTMLResponse

MIN_SIZE = 1
MAX_SIZE = 101
MIN_VAL = -1_000_000
MAX_VAL = 1_000_001
OAPI_PATH = "/docs"
RDOC_PATH = "/redocs"

app = FastAPI(docs_url=OAPI_PATH, redoc_url=RDOC_PATH)


@app.get("/", response_class=HTMLResponse)
async def get_root():
    """Root page."""

    return f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Root</title>
        </head>
        <body>
            <p>Docs at <ul>
                <li><a href="{OAPI_PATH}">{OAPI_PATH}<a></li>
                <li><a href="{RDOC_PATH}">{RDOC_PATH}<a></li>
            </ul></p>
        </body>
    </html>
    """


@app.get("/rng/ints/{size}")
async def get_rng_ints_SIZE(
    size: Annotated[int, Path(ge=MIN_SIZE, lt=MAX_SIZE)],
    start: Annotated[int, Query(ge=MIN_VAL, lt=MIN_VAL)],
    stop: Annotated[int, Query(ge=MIN_VAL, lt=MIN_VAL)],
):
    """
    Get list of random integers.
    - **size (path)**: Number of random integers that the list will contain.
    - **start (query)**: Minimum value of the random integers (inclusive).
    - **stop (query)**: Maximum value of the random integers (exclusive).
    """
    if stop - start < 2:
        raise HTTPException(
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            f"({stop=}) must be at least ({start=}) plus 2",
        )

    return {"ints": [randrange(start, stop) for _ in range(size)]}
