from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from app.shared.enums import UserRole


class RegisterRequest(BaseModel):
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    password: str = Field(..., min_length=8, max_length=100)
    role: UserRole


class RegisterResponse(BaseModel):
    message: str
    user_id: UUID


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    phone: str
    role: UserRole

    class Config:
        from_attributes = True