from pydantic import BaseModel


class BookTickets(BaseModel):
    id:str
    name:str
    amount:str

class RegUser(BaseModel):
    username:str
    PASSWORD:str

class login(BaseModel):
    userid:str
    password:str