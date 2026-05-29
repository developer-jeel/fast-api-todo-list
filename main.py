from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id : int
    name : str
    description : str

todos = []

@app.get('/')
def show_todos():
    return todos

@app.post('/')
def create_todos(todo : ToDo):
    todos.append(todo)
    return {"message" : "todo created sucessfully"}

@app.put('/{todo_id}')
def update_todos():
    return {"message" : "todo updated sucessfully"}