from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel
from datetime import datetime

from app.db.database import get_db, Todo

router = APIRouter(prefix="/api/v1/todos", tags=["todos"])

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    completed: int = 0

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str | None
    completed: int
    created_at: datetime

@router.post("/", response_model=TodoResponse, status_code=201)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    """Create a new Todo item"""
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/", response_model=List[TodoResponse])
def get_todos(db: Session = Depends(get_db)):
    """Get all Todo items"""
    return db.query(Todo).all()

@router.get("/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    """Get a single Todo by ID"""
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo
