from uuid import UUID

from pydantic import BaseModel, EmailStr, Field

from app.shared.enums import UserRole


# ==========================
# Register Schemas
# ==========================

class RegisterRequest(BaseModel):
    email: EmailStr
    phone: str = Field(..., min_length=10, max_length=15)
    password: str = Field(..., min_length=8, max_length=100)
    role: UserRole


class RegisterResponse(BaseModel):
    message: str
    user_id: UUID


# ==========================
# Login Schemas
# ==========================

class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=100)


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ==========================
# User Response Schema
# ==========================

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    phone: str
    role: UserRole

    class Config:
        from_attributes = True