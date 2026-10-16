
import json
from pathlib import Path

from models.patient import Patient
from rules.hypotension import HypotensionRule
from rules.tachycardia import HighHeartRateRule
from rules.tachypnoea import HighRespiratoryRateRule
from rules.low_sats import LowSatsRule
from rules.fever import FeverRule
from rules.hypertension import HypertensionRule
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
        LowSatsRule(),
        FeverRule(),
        HypertensionRule(),
    ])

    passed = 0

    report_results = []
    
    for scenario in scenarios:
        patient = Patient(**scenario["patient"])
        results = engine.evaluate(patient)

        actual_rules = sorted(
            result.rule_id for result in results
        )
        expected_rules = sorted(
            scenario["expected_rules"]
        )

        passed = actual_rules == expected_rules

        report_results.append({
            "scenario_id": scenario["scenario_id"],
            "description": scenario["description"],
            "expected_rules": expected_rules,
            "actual_rules": actual_rules,
            "passed": passed,
        })

        print(f"\n{scenario['scenario_id']}: "
            f"{scenario['description']}")
        print(f"Expected: {expected_rules}")
        print(f"Actual:   {actual_rules}")
        print(f"Result:   {'PASS' if passed else 'FAIL'}")

    print(f"\nEvaluation: {passed}/{len(scenarios)} scenarios passed.")

    report_path = project_root / "reports" / "evaluation_report.json"
    report_path.parent.mkdir(parents=True, exist_ok=True)

    with open(report_path, "w", encoding="utf-8") as file:
        json.dump(report_results, file, indent=2)

    print(f"\nReport saved to: {report_path}")





    total = len(report_results)
    passed_count = sum(
            1 for result in report_results if result["passed"]
        )
    failed_count = total - passed_count

    pass_rate = (
            passed_count / total * 100
            if total > 0
            else 0.0
        )

    print("\nSynthetic scenario evaluation")
    print("-----------------------------")
    print(f"Total scenarios: {total}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Pass rate: {pass_rate:.1f}%")



if __name__ == "__main__":
    main()