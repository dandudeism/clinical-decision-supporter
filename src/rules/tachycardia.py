
from models.patient import Patient
from rules.base import ClinicalRule, RuleResult


class HighHeartRateRule(ClinicalRule):
    def __init__(self, threshold: int = 100):
        self.threshold = threshold

    def evaluate(self, patient: Patient) -> RuleResult | None:
        if patient.heart_rate is None:
            return None
        
        if patient.heart_rate > self.threshold:
            return RuleResult(
                rule_id="HIGH_HEART_RATE",
                message=(
                    "Heart rate is above "
                    "the configured threshold."
                ),
                severity="medium"
            )

        return None
