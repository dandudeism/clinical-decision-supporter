An educational prototype for research exploring explainable, rule-based clinical decision support using Python and AI. This project is not intended for clinical use but could form the basis of clinical systems in the future.

This protype project contains a scenario evaluator that compares the returned alert IDs to the expected alert IDs defined in data/scenarios.json

To run the evaluation, from the project root, run:
$env:PYTHONPATH="src"
python src/evaluate_scenarios.py

This will print the passed or failed scenarios and save it to reports/evaluation_report.json

Limitations: The dataset in this protype is falsified. Passing the evaluation simply means the model matches precoded expectations and doesn't necessarily demonstarate clinical accuracy but is a start in the right direction.

The scoring thresholds for example are purely educational, adapted from established NEWS scoring data.