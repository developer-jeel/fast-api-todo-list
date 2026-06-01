from fastapi import APIRouter,Depends,HTTPException
from pydantic import BaseModel

router = APIRouter()
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
def update_todos(todo_id:int , updated_todo : ToDo):
    for i , todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message" : "todo updated sucessfully"}
    return {"message" : "feild todo"}

@app.delete('/{todo_id}')
def delete_todos(todo_id:int):
    global todos
    todos = [todo for todo in todos if todo.id != todo_id ]
    return {"message" : " todo deleted"}