
from models.patient import Patient
from rules.base import ClinicalRule, RuleResult


class LowSatsRule(ClinicalRule):
    def __init__(self, threshold: int = 92):
        self.threshold = threshold

    def evaluate(self, patient: Patient) -> RuleResult | None:
        if patient.sats is None:
            return None
        
        if patient.sats < self.threshold and patient.sats > 87:
            return RuleResult(
                rule_id="LOW_SATS_1",
                message=(
                    "Sats are below "
                    "the configured threshold."
                ),
                severity="medium"
            )
        elif patient.sats <= 87:
            return RuleResult(
                rule_id="LOW_SATS_2",
                message=(
                    "Sats are below "
                    "the configured threshold."
                ),
                severity="high"
            )

        return None
