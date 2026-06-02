from fastapi import APIRouter,Depends,HTTPException
from pydantic import BaseModel
from database import *
from sqlalchemy.orm import Session
from models import ToDo
from typing import List,Optional

from fastapi import Form , Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()

templates = Jinja2Templates(directory='templates')
class ToDoCreate(BaseModel):
    title : str
    description : Optional[str]
    done : bool

class ToDoResponse(ToDoCreate):
    id : int

@router.get('/')
def show_todos(request : Request, db : Session = Depends(get_db)):
    todos = db.query(ToDo).all()
    return templates.TemplateResponse(request, name='todo_list.html', context={"request": request, "todos": todos})

@router.get('/create')
def create_page(request : Request):
    return templates.TemplateResponse(request, 'create_todo.html', context={"request": request})
    
@router.post('/create')
def create_todos(
    title: str = Form(...),
    description: str = Form(...),
    done: bool = Form(False),
    db: Session = Depends(get_db)):
    new_todo = ToDo(title=title, description=description, done=done)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return RedirectResponse(url='/todo/', status_code=303)

@router.get('/update/{todo_id}')
def update_todos(request : Request ,todo_id:int,db : Session = Depends(get_db)):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not todo:
        return HTTPException(status_code=404,detail="Todo not found")
    return templates.TemplateResponse(request, 'update.html', context={"request": request, "todo": todo})

@router.post('/update/{todo_id}')
def update_todo(todo_id:int,
    title: str = Form(...),
    description: str = Form(...),
    done: bool = Form(False),
    db : Session = Depends(get_db)):
    db_todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not db_todo:
        return HTTPException(status_code=404,detail="Todo not found")
    
    db_todo.title = title
    db_todo.description = description
    db_todo.done = done
    db.commit()
    return RedirectResponse(url="/todo/", status_code=303)

@router.get('/delete/{todo_id}')
def delete_todos(request: Request,todo_id:int,db : Session = Depends(get_db)):
    db_todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    if not db_todo:
        return HTTPException(status_code=404,detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return RedirectResponse(url="/todo/", status_code=303)