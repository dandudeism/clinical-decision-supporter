import json
from pathlib import Path

from models.patient import Patient
from rules.hypotension import HypotensionRule
from rules.tachycardia import HighHeartRateRule
from rules.tachypnoea import HighRespiratoryRateRule
from rules.fever import FeverRule
from rules.hypertension import HypertensionRule
from rules.low_sats import LowSatsRule
from engine import DecisionEngine


def test_all_synthetic_scenarios_match_expected_rules():
    project_root = Path(__file__).resolve().parent.parent
    scenarios_path = project_root / "data" / "scenarios.json"

    with scenarios_path.open(encoding="utf-8") as file:
        scenarios = json.load(file)

    engine = DecisionEngine([
        HypotensionRule(),
        HighHeartRateRule(),
        HighRespiratoryRateRule(),
        LowSatsRule(),
        FeverRule(),
        HypertensionRule(),
    ])

    for scenario in scenarios:
        patient = Patient(**scenario["patient"])
        results = engine.evaluate(patient)

        actual = sorted(
            result.rule_id for result in results
        )
        expected = sorted(scenario["expected_rules"])

        assert actual == expected, scenario["id"]


def test_scenario_ids_are_unique():
    project_root = Path(__file__).resolve().parent.parent
    scenarios_path = project_root / "data" / "scenarios.json"

    with open(scenarios_path, encoding="utf-8") as file:
        scenarios = json.load(file)

    scenario_ids = [
        scenario["scenario_id"]
        for scenario in scenarios
    ]

    assert len(scenario_ids) == len(set(scenario_ids))
