from pydantic import BaseModel

class user_create(BaseModel):
    id : int
    name: str
    role: str
    password: str

class user_response(BaseModel):
    id: int
    name: str
    role: str

class user_update(BaseModel):
    id: int=None
    name: str=None
   

    
