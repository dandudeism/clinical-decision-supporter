
from models.patient import Patient
from rules.base import ClinicalRule, RuleResult


class FeverRule(ClinicalRule):
    def __init__(self, threshold: float = 37.8):
        self.threshold = threshold

    def evaluate(self, patient: Patient) -> RuleResult | None:
        if patient.temperature is None:
            return None
        
        if patient.temperature > self.threshold:
            return RuleResult(
                rule_id="HIGH_TEMPERATURE",
                message=(
                    "Temperature is above "
                    "the configured threshold."
                ),
                severity="high"
            )

        return None
