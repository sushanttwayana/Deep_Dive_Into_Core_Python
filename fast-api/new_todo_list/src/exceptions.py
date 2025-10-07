from fastapi import HTTPException

class TodoError(HTTPException):
    """Base exception for todo-related errors"""
    pass

class TodoNotFoundError(TodoError):
    def __init__(self, todo_id):
        message = "Todo not found" if todo_id is None else f"Todo with id {todo_id} not found"
        super().__init__(status_code=404, detail=message)

class TodoCreationError(TodoError):
    def __init__(self, error: str):
        message = "Failed to create todo" if error is None else f"Failed to create todo: {error}"
        super().__init__(status_code=500, detail=message)

class UserError(HTTPException):
    """Base exception for user-related errors"""
    pass

class UserNotFoundError(UserError):
    def __init__(self, user_id):
        message = "User not found" if user_id is None else f"User with id {user_id} not found"
        super().__init__(status_code=404, detail=message)

class PasswordMismatchError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="New passwords do not match")
        
class InvalidPasswordError(UserError):
    def __init__(self):
        super().__init__(status_code=400, detail="Current Password is Incorrect")
        
class AuthenticationError(UserError):
    def __init__(self, message:str = "Could not validate user"):
        super().__init__(status_code=401, detail=message)
        
