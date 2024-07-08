from fastapi import FastAPI
from .routers import users
from .routers.langchain import chain

from langserve import add_routes

# 4. App definition
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

app.include_router(users.router, prefix="/users", tags=["users"])

add_routes(
    app,
    chain,
    path="/chain",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI MongoDB example!"}
