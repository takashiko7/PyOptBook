#エントリーポイント
from fastapi import FastAPI
from .routers import optimize

app = FastAPI()

app.include_router(optimize.router)
