from uuid import UUID

from sqlalchemy.orm import Session

from app.modules.patient.model import Patient


class PatientRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_patient_by_id(self, patient_id: UUID) -> Patient | None:
        """
        Retrieve a patient using user UUID.
        """
        return (
            self.db.query(Patient)
            .filter(Patient.id == patient_id)
            .first()
        )

    def create_patient(self, patient: Patient) -> Patient:
        """
        Save a new patient profile.
        """
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient

    def update_patient(self, patient: Patient) -> Patient:
        """
        Update an existing patient profile.
        """
        self.db.commit()
        self.db.refresh(patient)
        return patient