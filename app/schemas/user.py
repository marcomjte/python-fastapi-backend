# app/schemas/user.py
from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    email:    EmailStr
    password: str

class UserResponse(BaseModel):
    id:           str
    name:         str
    email:        str
    access_token: str

class MeResponse(BaseModel):
    id:    int
    name:  str
    email: str

    class Config:
        from_attributes = True