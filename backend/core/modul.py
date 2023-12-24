from pydantic import BaseModel, EmailStr

class sign_up_reset(BaseModel):
    email: EmailStr
    username: str
    password: str
    driver:bool

class caller(BaseModel):
    origin: str
    destination:str
