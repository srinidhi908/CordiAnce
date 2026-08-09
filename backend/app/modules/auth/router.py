from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.repository import AuthRepository
from app.modules.auth.roles import require_role
from app.modules.auth.schema import (
    LoginRequest,
    LoginResponse,
    RegisterRequest,
    RegisterResponse,
    UserResponse,
)
from app.modules.auth.service import AuthService
from app.shared.enums import UserRole


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=RegisterResponse,
)
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
):
    repository = AuthRepository(db)

    service = AuthService(repository)

    user = service.register_user(request)

    return RegisterResponse(
        message="User registered successfully.",
        user_id=user.id,
    )


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    repository = AuthRepository(db)

    service = AuthService(repository)

    return service.login_user(request)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_me(
    current_user=Depends(get_current_user),
):
    return current_user


@router.get(
    "/doctor-test",
)
def doctor_test(
    current_user=Depends(
        require_role(UserRole.DOCTOR)
    ),
):
    return {
        "message": "Doctor access granted.",
        "user_id": str(current_user.id),
        "role": current_user.role.value,
    }