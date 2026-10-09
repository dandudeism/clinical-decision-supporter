from pydantic import BaseModel, Field

class Patient(BaseModel):
    age: int = Field(ge=0, le=120)
    heart_rate: int = Field(gt=0, le=300)
    systolic_bp: int = Field(gt=0, le=300)
    temperature: float = Field(gt=20, lt=50)
    resp_rate: int = Field(gt=0, le=100)
    sats: int = Field(ge=0, le=100)
    confusion: bool