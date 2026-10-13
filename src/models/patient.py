from pydantic import BaseModel, Field

class Patient(BaseModel):
    age: int = Field(ge=0, le=120)
    heart_rate: int | None = Field(default=None, gt=0, le=300)
    systolic_bp: int | None = Field(default=None, gt=0, le=300)
    temperature: float | None = Field(default=None, gt=20, lt=50)
    resp_rate: int | None = Field(default=None, gt=0, le=100)
    sats: int | None = Field(default=None, ge=0, le=100)
    confusion: bool | None = None