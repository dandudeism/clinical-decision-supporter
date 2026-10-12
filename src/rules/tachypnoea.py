
from models.patient import Patient
from rules.base import ClinicalRule, RuleResult


class HighRespiratoryRateRule(ClinicalRule):
    def __init__(self, threshold: int = 20):
        self.threshold = threshold

    def evaluate(self, patient: Patient) -> RuleResult | None:
        if patient.resp_rate > self.threshold:
            return RuleResult(
                rule_id="HIGH_RESPIRATORY_RATE",
                message=(
                    "Respiratory rate is above "
                    "the configured threshold."
                ),
                severity="medium"
            )

        return None
