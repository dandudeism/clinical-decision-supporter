import pytest
from pydantic import ValidationError

from models.patient import Patient

def test_valid_patient_is_created():
    patient = Patient(
        age=55,
        heart_rate=87,
        systolic_bp=130,
        temperature=37.1,
        resp_rate=16,
        sats=97,
        confusion=False
    )
    assert patient.age == 55
    assert patient.heart_rate == 87

def test_negative_age_is_rejected():
    with pytest.raises(ValidationError):
        Patient(
            age=-5,
            heart_rate=80,
            systolic_bp=120,
            temperature=36.8,
            resp_rate=16,
            sats=98,
            confusion=False
        )

def test_oxygen_saturation_above_100_is_rejected():
    with pytest.raises(ValidationError):
        Patient(
            age=40,
            heart_rate=80,
            systolic_bp=120,
            temperature=36.8,
            resp_rate=16,
            sats=150,
            confusion=False
        )