from datetime import datetime, timezone
from uuid import uuid4, UUID
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.auth.models import TokenData
from src.entities.todo import Todo
from src.exceptions import TodoCreationError, TodoNotFoundError
from logging import info as _info
from . import model

def create_todo(current_user: TokenData, db: Session, todo: model.TodoCreate) -> Todo:
    try:
        new_todo = Todo(**todo.model_dump())
        new_todo.user_id = current_user.get_uuid()
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        _info(f"Created new todo for user: {current_user.get_uuid()}")
        return new_todo
    except Exception as e:
        _info(f"Failed to create todo for user {current_user.get_uuid()}. E"
              f"rror: {str(e)}")
        raise TodoCreationError(str(e))

def get_todos_by_current_user(current_user: TokenData, db: Session) -> list[model.TodoResponse]:
    todos = db.query(Todo).filter(Todo.user_id == current_user.get_uuid()).all()
    _info(f"Retrieved {len(todos)} todos for user: {current_user.get_uuid()}")
    return todos

def get_todo_by_id(current_user: TokenData, db: Session, todo_id: UUID) -> Todo:
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == current_user.get_uuid()).first()
    if not todo:
        _info(f"Warning: Todo {todo_id} not found for user: {current_user.get_uuid()}")
        raise TodoNotFoundError(todo_id)
    _info(f"Retrieved todo {todo_id} for user {current_user.get_uuid()}")
    return todo

def update_todo(current_user: TokenData, db: Session, todo_id: UUID, todo_update: model.TodoCreate) -> Todo:
    todo_data = todo_update.model_dump(exclude_unset=True)
    db.query(Todo).filter(Todo.id == todo_id, Todo.user_id == current_user.get_uuid())\
        .update(todo_data)
    db.commit()
    _info(f"Successfully updated todo {todo_id} for user {current_user.get_uuid()}")
    return get_todo_by_id(current_user, db, todo_id)

def complete_todo(current_user: TokenData, db: Session, todo_id: UUID) -> Todo:
    todo = get_todo_by_id(current_user, db, todo_id)
    if todo.is_completed:
        _info(f"debug: {todo_id} is already completed")
        return todo
    todo.completed_at = datetime.now(timezone.utc)
    todo.is_completed = True
    db.commit()
    _info(f"Todo {todo_id} marked as completed by user {current_user.get_uuid()}")
    return todo

def delete_todo(current_user: TokenData, db: Session, todo_id: UUID) -> None:
    todo = get_todo_by_id(current_user, db, todo_id)
    db.delete(todo)
    db.commit()
    _info(f"Todo {todo_id} deleted by user {current_user.get_uuid()}")