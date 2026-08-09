from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.modules.auth.dependencies import get_current_user
from app.modules.auth.model import User
from app.modules.patient.repository import PatientRepository
from app.modules.patient.schema import (
    PatientCreateRequest,
    PatientResponse,
)
from app.modules.patient.service import PatientService

router = APIRouter(
    prefix="/patient",
    tags=["Patient"],
)


@router.post(
    "/profile",
    response_model=PatientResponse,
)
def create_patient_profile(
    request: PatientCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repository = PatientRepository(db)
    service = PatientService(repository)

    return service.create_patient(
        user_id=current_user.id,
        request=request,
    )


@router.get(
    "/profile",
    response_model=PatientResponse,
)
def get_patient_profile(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repository = PatientRepository(db)
    service = PatientService(repository)

    return service.get_patient(
        user_id=current_user.id,
    )


@router.put(
    "/profile",
    response_model=PatientResponse,
)
def update_patient_profile(
    request: PatientCreateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repository = PatientRepository(db)
    service = PatientService(repository)

    return service.update_patient(
        user_id=current_user.id,
        request=request,
    )