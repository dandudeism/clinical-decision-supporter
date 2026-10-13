
from models.patient import Patient
from rules.hypotension import HypotensionRule
from rules.tachypnoea import HighRespiratoryRateRule
from rules.tachycardia import HighHeartRateRule
from engine import DecisionEngine
from scoring import calculate_risk


patient = Patient(
    age=67,
    heart_rate=125,
    systolic_bp=82,
    temperature=36.7,
    resp_rate=24,
    sats=94,
    confusion=True
)

engine = DecisionEngine(
    rules=[
        HypotensionRule(),
        HighHeartRateRule(),
        HighRespiratoryRateRule()   
    ]
)

results = engine.evaluate(patient)

assessment = calculate_risk(results)
print(f"Risk score: {assessment.score}")
print(f"Category: {assessment.category}")
print(f"Triggered rules: {assessment.triggered_rules}")

if not results:
    print("No rules triggered.")
else:
    print(f"{len(results)} alert(s) triggered: \n")

    for result in results:
        print(f"Rule: {result.rule_id}")
        print(f"Message: {result.message}")
        print(f"Severity: {result.severity}")
        print("-" * 30)
