from api.auth import router as api_router

from fastapi import FastAPI
import uvicorn

app = FastAPI()

app.include_router(api_router, prefix='/api')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)