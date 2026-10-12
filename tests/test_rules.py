from models.patient import Patient
from rules.hypotension import HypotensionRule
from rules.tachycardia import HighHeartRateRule
from rules.tachypnoea import HighRespiratoryRateRule

def make_patient(systolic_bp: int) -> Patient:
    return Patient(
        age=55,
        heart_rate=67,
        systolic_bp=systolic_bp,
        temperature=36.8,
        resp_rate=16,
        sats=93,
        confusion=False

    )

def test_rule_triggers_below_threshold():
    patient = make_patient(83)
    rule = HypotensionRule()

    result = rule.evaluate(patient)

    assert result is not None
    assert result.rule_id == "LOW_SYSTOLIC_BP"


def test_rule_does_not_trigger_above_threshold():
    patient = make_patient(110)
    rule = HypotensionRule()

    result = rule.evaluate(patient)

    assert result is None


def test_rule_does_not_trigger_at_threshold():
    patient = make_patient(90)
    rule = HypotensionRule()

    result = rule.evaluate(patient)

    assert result is None