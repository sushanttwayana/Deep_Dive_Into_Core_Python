from fastapi import FastAPI, Depends
from typing import Annotated

app =FastAPI()

class Logger:
    
    def log(self, message:str):
        print(f"Logging message: {message}")

def get_logger():
    return Logger()    

# @app.get("/log/{message}")
# def log_message(message: str):
#     logger = Logger() # each time we need to instansiate this  so we can limit this
#     logger.log(message)
#     return message


logger_dependency = Annotated[Logger, Depends(get_logger)]

"""WE can replace the above one with the dependency injection """
@app.get("/log/{message}")
# def log_message(message: str, logger: Logger = Depends(get_logger)):
def log_message(message: str,logger: logger_dependency): 
    logger.log(message)
    return message