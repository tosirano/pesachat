import logging

import uvicorn
from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI(title="pesachat-core", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "pesachat-core", "version": "0.1.0"}


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    uvicorn.run("pesachat_core.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
