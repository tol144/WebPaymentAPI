import asyncio
import uvicorn

from config import settings
from api.app import create_fastapi_app


app = create_fastapi_app()

async def main():
    pass


if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run(
        app="main:app",
        reload=True,
        host=settings.uvicorn_host,
        port=settings.uvicorn_port,
    )
