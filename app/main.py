from fastapi import FastAPI
from .routers import users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI MongoDB example!"}


@app.post("/ask")
def ask_question(query: str, history: list = []):
    try:
        answer = get_answer(query, history)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))