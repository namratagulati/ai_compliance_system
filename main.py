from fastapi import FastAPI
#Server startup
from api.routes import router

app = FastAPI(
    title="AI Compliance System"
)

app.include_router(router)