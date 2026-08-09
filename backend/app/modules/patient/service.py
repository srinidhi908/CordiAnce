from uuid import UUID

from fastapi import HTTPException, status

from app.modules.patient.model import Patient
from app.modules.patient.repository import PatientRepository
from app.modules.patient.schema import (
    PatientCreateRequest,
    PatientResponse,
)


class PatientService:

    def __init__(self, repository: PatientRepository):
        self.repository = repository

    def create_patient(
        self,
        user_id: UUID,
        request: PatientCreateRequest,
    ) -> PatientResponse:

        # Check whether a patient profile already exists
        existing_patient = self.repository.get_patient_by_id(user_id)

        if existing_patient:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Patient profile already exists.",
            )

        # Create patient profile using the authenticated user's ID
        patient = Patient(
            id=user_id,
            age=request.age,
            gender=request.gender,
            blood_group=request.blood_group,
            height=request.height,
            weight=request.weight,
            allergies=request.allergies,
            emergency_contact=request.emergency_contact,
        )

        return self.repository.create_patient(patient)

    def get_patient(
        self,
        user_id: UUID,
    ) -> PatientResponse:

        patient = self.repository.get_patient_by_id(user_id)

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient profile not found.",
            )

        return patient

    def update_patient(
        self,
        user_id: UUID,
        request: PatientCreateRequest,
    ) -> PatientResponse:

        patient = self.repository.get_patient_by_id(user_id)

        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Patient profile not found.",
            )

        patient.age = request.age
        patient.gender = request.gender
        patient.blood_group = request.blood_group
        patient.height = request.height
        patient.weight = request.weight
        patient.allergies = request.allergies
        patient.emergency_contact = request.emergency_contact

        return self.repository.update_patient(patient)