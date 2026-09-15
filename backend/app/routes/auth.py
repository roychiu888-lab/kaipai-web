from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: dict

@router.post("/login", response_model=LoginResponse)
async def login(credentials: LoginRequest):
    """User login"""
    return {
        "access_token": "fake-jwt-token",
        "token_type": "bearer",
        "user": {"id": "1", "email": credentials.email}
    }

@router.post("/logout")
async def logout():
    """User logout"""
    return {"message": "Logged out successfully"}

@router.post("/register")
async def register(credentials: LoginRequest):
    """User registration"""
    return {
        "message": "User registered",
        "user": {"id": "1", "email": credentials.email}
    }
