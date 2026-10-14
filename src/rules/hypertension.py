
from models.patient import Patient
from rules.base import ClinicalRule, RuleResult


class HypertensionRule(ClinicalRule):
    def __init__(self, threshold: int = 180):
        self.threshold = threshold

    def evaluate(self, patient: Patient) -> RuleResult | None:
        if patient.systolic_bp is None:
            return None
        
        if patient.systolic_bp > self.threshold:
            return RuleResult(
                rule_id="HIGH_SYSTOLIC_BP",
                message=(
                    "Systolic blood pressure is above "
                    "the configured threshold."
                ),
                severity="high"
            )

        return None
