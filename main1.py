from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database1 import engine
from models1 import users
from sqlalchemy import insert, select

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register(user: User):
    with engine.begin() as conn:  # Ensures data is committed
        result = conn.execute(select(users).where(users.c.username == user.username)).fetchone()
        if result:
            raise HTTPException(status_code=400, detail="Username already exists")
        conn.execute(insert(users).values(username=user.username, password=user.password))
        return {"message": "User registered successfully"}

@app.get("/users")
def list_users():
    with engine.connect() as conn:
        result = conn.execute(select(users))
        return [dict(row._mapping) for row in result.fetchall()]
# This code provides a simple user registration and listing API using FastAPI and SQLAlchemy.