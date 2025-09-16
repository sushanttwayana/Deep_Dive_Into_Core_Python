from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

class EmailService:
    
    def send_email(self, recipient:str, message:str):
        print(f"Sending email to {recipient} : {message}")
        

def get_email_service():
    return EmailService()

email_service_dependency = Annotated[EmailService, Depends(get_email_service)]

def send_email(recipient:str, message:str, email_service: email_service_dependency):
    email_service.send_email(recipient, message)