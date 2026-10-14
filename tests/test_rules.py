from models.patient import Patient
from rules.hypotension import HypotensionRule
from rules.tachycardia import HighHeartRateRule
from rules.tachypnoea import HighRespiratoryRateRule
from rules.fever import FeverRule
from rules.hypertension import HypertensionRule
from rules.low_sats import LowSatsRule

def make_patient(**overrides):
    data = {
        "age": 40,
        "heart_rate": 75,
        "systolic_bp": 120,
        "temperature": 36.7,
        "resp_rate": 16,
        "sats": 98,
        "confusion": False,
    }
    data.update(overrides)
    return Patient(**data)


def test_rule_triggers_below_threshold():
    patient = make_patient(systolic_bp=83)
    rule = HypotensionRule()

    result = rule.evaluate(patient)

    assert result is not None
    assert result.rule_id == "LOW_SYSTOLIC_BP"


def test_rule_does_not_trigger_above_threshold():
    patient = make_patient(systolic_bp=110)
    rule = HypotensionRule()

    result = rule.evaluate(patient)

    assert result is None


def test_rule_does_not_trigger_at_threshold():
    patient = make_patient(systolic_bp=90)
    rule = HypotensionRule()

    result = rule.evaluate(patient)

    assert result is None

# Tachycardia Rule tests

def test_high_heart_rate_rule_triggers():
    patient = make_patient(systolic_bp=110)
    patient.heart_rate = 120

    result = HighHeartRateRule().evaluate(patient)

    assert result is not None
    assert result.rule_id == "HIGH_HEART_RATE"


def test_high_heart_rate_rule_does_not_trigger():
    patient = make_patient(systolic_bp=110)
    patient.heart_rate = 80

    result = HighHeartRateRule().evaluate(patient)

    assert result is None

# HighRespRate tests

def test_high_respiratory_rate_rule_triggers():
    patient = make_patient(systolic_bp=110)
    patient.resp_rate = 25

    result = HighRespiratoryRateRule().evaluate(patient)

    assert result is not None
    assert result.rule_id == "HIGH_RESPIRATORY_RATE"


def test_high_respiratory_rate_rule_does_not_trigger():
    patient = make_patient(systolic_bp=110)
    patient.resp_rate = 16

    result = HighRespiratoryRateRule().evaluate(patient)

    assert result is None

# HypotensionRule tests

def test_hypotension_rule_handles_missing_blood_pressure():
    patient = Patient(age=67, systolic_bp=None)

    result = HypotensionRule().evaluate(patient)

    assert result is None


def test_hypotension_rule_triggers_below_threshold():
    patient = Patient(age=67, systolic_bp=81)

    result = HypotensionRule().evaluate(patient)

    assert result is not None
    assert result.rule_id == "LOW_SYSTOLIC_BP"


def test_hypotension_rule_does_not_trigger_at_threshold():
    patient = Patient(age=67, systolic_bp=85)

    result = HypotensionRule().evaluate(patient)

    assert result is None

# FeverRule tests

def test_fever_rule_triggers_above_threshold():
    rule = FeverRule()
    patient = make_patient(temperature=39.0)

    result = rule.evaluate(patient)

    assert result is not None
    assert result.rule_id == "HIGH_TEMPERATURE"
    assert result.severity == "high"


def test_fever_rule_does_not_trigger_below_threshold():
    rule = FeverRule()
    patient = make_patient(temperature=36.7)

    result = rule.evaluate(patient)

    assert result is None


def test_fever_rule_does_not_trigger_at_threshold():
    rule = FeverRule()
    patient = make_patient(temperature=37.8)

    result = rule.evaluate(patient)

    assert result is None


def test_fever_rule_handles_missing_temperature():
    rule = FeverRule()
    patient = make_patient(temperature=None)

    result = rule.evaluate(patient)

    assert result is None


# HypertensionRule tests

def test_hypertension_rule_triggers_above_threshold():
    rule = HypertensionRule()
    patient = make_patient(systolic_bp=200)

    result = rule.evaluate(patient)

    assert result is not None
    assert result.rule_id == "HIGH_SYSTOLIC_BP"
    assert result.severity == "high"


def test_hypertension_rule_does_not_trigger_below_threshold():
    rule = HypertensionRule()
    patient = make_patient(systolic_bp=120)

    result = rule.evaluate(patient)

    assert result is None


def test_hypertension_rule_does_not_trigger_at_threshold():
    rule = HypertensionRule()
    patient = make_patient(systolic_bp=180)

    result = rule.evaluate(patient)

    assert result is None


def test_hypertension_rule_handles_missing_blood_pressure():
    rule = HypertensionRule()
    patient = make_patient(systolic_bp=None)

    result = rule.evaluate(patient)

    assert result is None

# LowSatsRule tests

def test_low_sats_rule_triggers():
    patient = make_patient(sats=88)
    result = LowSatsRule().evaluate(patient)

    assert result is not None
    assert result.rule_id == "LOW_SATS_1"


def test_low_sats_rule_does_not_trigger():
    patient = make_patient(sats=98)
    result = LowSatsRule().evaluate(patient)

    assert result is None