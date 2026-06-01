from fastapi import APIRouter,Depends,HTTPException
from pydantic import BaseModel
from database import *
from sqlalchemy.orm import Session
from models import ToDo
from typing import List

router = APIRouter()
class ToDoCreate(BaseModel):
    title : str
    description : str
    done : bool

class ToDoResponse(ToDoCreate):
    id : int

todos = []

@router.get('/',response_model=List[ToDoResponse])
def show_todos(db : Session = Depends(get_db)):
    return db.query(ToDo).all()

@router.post('/',response_model=ToDoResponse)
def create_todos(todo : ToDoCreate,db : Session = Depends(get_db)):
    new_todo = ToDo(title = todo.title,description = todo.description,done = todo.done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

@router.put('/{todo_id}',response_model=ToDoResponse)
def update_todos(todo_id:int,todo : ToDoCreate ,db : Session = Depends(get_db)):
    

# @router.delete('/{todo_id}')
# def delete_todos(todo_id:int):
#     global todos
#     todos = [todo for todo in todos if todo.id != todo_id ]
#     return {"message" : " todo deleted"}