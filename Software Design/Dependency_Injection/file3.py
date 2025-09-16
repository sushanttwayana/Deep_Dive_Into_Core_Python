from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated

app = FastAPI()


class AuthService:
    
    def authenticate(self, token:str):
        
        # if token == "valid-token":
        if token == "123456789":
            return True
        
        else:           
            raise HTTPException(status_code = 401, detail= 'Unauthorized')
        
def get_auth_service():
    return AuthService()

auth_service_dependency = Annotated[AuthService, Depends(get_auth_service)]

@app.get("/secure-data/")
def get_secure_data(token: str, auth_service: auth_service_dependency):
    if auth_service.authenticate(token):
        return {"data": "This is secure data."}