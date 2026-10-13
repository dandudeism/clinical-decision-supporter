
import json
from pathlib import Path

from models.patient import Patient
from rules.hypotension import HypotensionRule
from rules.tachycardia import HighHeartRateRule
from rules.tachypnoea import HighRespiratoryRateRule
from engine import DecisionEngine
from scoring import calculate_risk

def main():
    project_root = Path(__file__).resolve().parent.parent
    scenarios_path = project_root / "data" / "scenarios.json"

    with scenarios_path.open(encoding="utf-8") as file:
        scenarios = json.load(file)

    engine = DecisionEngine([
        HypotensionRule(),
        HighHeartRateRule(),
        HighRespiratoryRateRule(),
    ])

    passed = 0

    for scenario in scenarios:
        patient = Patient(**scenario["patient"])
        results = engine.evaluate(patient)

        actual_rules = sorted(
            result.rule_id for result in results
        )
        expected_rules = sorted(
            scenario["expected_rules"]
        )

        assessment = calculate_risk(results)
        success = actual_rules == expected_rules

        if success:
            passed += 1

        print(f"\nScenario: {scenario['id']}")
        print(f"Description: {scenario['description']}")
        print(f"Expected rules: {expected_rules}")
        print(f"Actual rules:   {actual_rules}")
        print(f"Score: {assessment.score}")
        print(f"Category: {assessment.category}")
        print(f"Test passed: {success}")

    print(f"\nEvaluation: {passed}/{len(scenarios)} scenarios passed.")


if __name__ == "__main__":
    main()