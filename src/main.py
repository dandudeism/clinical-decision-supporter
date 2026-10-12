
from models.patient import Patient
from rules.hypotension import HypotensionRule
from engine import DecisionEngine


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
    rules=[HypotensionRule()]
)

results = engine.evaluate(patient)

for result in results:
    print(result.rule_id)
    print(result.message)
    print(result.severity)
