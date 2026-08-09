from uuid import UUID

from pydantic import BaseModel, Field


# ==========================
# Patient Profile Schemas
# ==========================

class PatientCreateRequest(BaseModel):
    age: int = Field(..., ge=0, le=150)
    gender: str = Field(..., min_length=1, max_length=20)
    blood_group: str = Field(..., min_length=1, max_length=10)
    height: float = Field(..., gt=0)
    weight: float = Field(..., gt=0)
    allergies: str | None = Field(
        default=None,
        max_length=500,
    )
    emergency_contact: str = Field(
        ...,
        min_length=10,
        max_length=20,
    )


class PatientResponse(BaseModel):
    id: UUID
    age: int
    gender: str
    blood_group: str
    height: float
    weight: float
    allergies: str | None
    emergency_contact: str

    class Config:
        from_attributes = True