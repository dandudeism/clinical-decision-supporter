from models.patient import Patient
from engine import DecisionEngine
from rules.hypotension import HypotensionRule

def make_patient(systolic_bp: int) -> Patient:
    return Patient(
        age=67,
        heart_rate=80,
        systolic_bp=systolic_bp,
        temperature=36.8,
        resp_rate=16,
        sats=98,
        confusion=False
    )

def test_engine_returns_triggered_rules():
    engine = DecisionEngine([HypotensionRule()])
    patient = make_patient(82)

    results = engine.evaluate(patient)

    assert len(results) == 1
    assert results[0].rule_id == "LOW_SYSTOLIC_BP"

def test_engine_returns_empty_list_when_no_rule_triggers():
    engine = DecisionEngine([HypotensionRule()])
    patient = make_patient(110)

    results = engine.evaluate(patient)

    assert results == []


def test_engine_with_no_rules():
    engine = DecisionEngine([])
    patient = make_patient(110)

    results = engine.evaluate(patient)

    assert results == []