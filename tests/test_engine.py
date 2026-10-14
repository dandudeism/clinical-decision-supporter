from models.patient import Patient
from engine import DecisionEngine
from rules.hypotension import HypotensionRule
from rules.tachycardia import HighHeartRateRule
from rules.tachypnoea import HighRespiratoryRateRule
from rules.fever import FeverRule
from rules.low_sats import LowSatsRule
from rules.hypertension import HypertensionRule


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

def test_engine_returns_triggered_rules():
    engine = DecisionEngine([HypotensionRule()])
    patient = make_patient(systolic_bp=82)

    results = engine.evaluate(patient)

    assert len(results) == 1
    assert results[0].rule_id == "LOW_SYSTOLIC_BP"

def test_engine_returns_empty_list_when_no_rule_triggers():
    engine = DecisionEngine([HypotensionRule()])
    patient = make_patient(systolic_bp=110)

    results = engine.evaluate(patient)

    assert results == []


def test_engine_with_no_rules():
    engine = DecisionEngine([])
    patient = make_patient(systolic_bp=110)

    results = engine.evaluate(patient)

    assert results == []

def test_engine_returns_multiple_triggered_rules():
    patient = Patient(
        age=67,
        heart_rate=125,
        systolic_bp=82,
        temperature=38.7,
        resp_rate=24,
        sats=94,
        confusion=True
    )

    engine = DecisionEngine([
        HypotensionRule(),
        HighHeartRateRule(),
        HighRespiratoryRateRule()
    ])

    results = engine.evaluate(patient)
    rule_ids = {result.rule_id for result in results}

    assert len(results) == 3
    assert rule_ids == {
        "LOW_SYSTOLIC_BP",
        "HIGH_HEART_RATE",
        "HIGH_RESPIRATORY_RATE"
    }

def test_engine_returns_new_alerts():
    patient = make_patient(
        temperature=39.0,
        systolic_bp=190,
        sats=84,
    )

    engine = DecisionEngine([
        FeverRule(),
        HypertensionRule(),
        LowSatsRule(),
    ])

    results = engine.evaluate(patient)
    rule_ids = {result.rule_id for result in results}

    assert rule_ids == {
        "HIGH_TEMPERATURE",
        "HIGH_SYSTOLIC_BP",
        "LOW_SATS_2",
    }