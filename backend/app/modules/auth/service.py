from datetime import timedelta

from fastapi import HTTPException, status

from app.core.config import settings
from app.modules.auth.model import User
from app.modules.auth.repository import AuthRepository
from app.modules.auth.schema import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
)
from app.modules.auth.utils import (
    create_access_token,
    hash_password,
    verify_password,
)


class AuthService:

    def __init__(self, repository: AuthRepository):
        self.repository = repository

    def register_user(self, request: RegisterRequest) -> User:

        # Check if email already exists
        if self.repository.get_user_by_email(request.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered.",
            )

        # Check if phone already exists
        if self.repository.get_user_by_phone(request.phone):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Phone number already exists.",
            )

        # Create new user
        user = User(
            email=request.email,
            phone=request.phone,
            password_hash=hash_password(request.password),
            role=request.role,
        )

        return self.repository.create_user(user)

    def login_user(self, request: LoginRequest) -> LoginResponse:

        # Find user by email
        user = self.repository.get_user_by_email(request.email)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        # Verify password
        if not verify_password(
            request.password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
            )

        # Create JWT access token
        access_token = create_access_token(
            data={
                "sub": str(user.id),
                "email": user.email,
                "role": user.role.value,
            },
            expires_delta=timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
            ),
        )

        return LoginResponse(
            access_token=access_token,
            token_type="bearer",
        )