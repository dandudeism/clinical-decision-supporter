
from models.patient import Patient
from rules.base import ClinicalRule, RuleResult


class HypotensionRule(ClinicalRule):
    def __init__(self, threshold: int = 85):
        self.threshold = threshold

    def evaluate(self, patient: Patient) -> RuleResult | None:
        if patient.systolic_bp is None:
            return None
        
        if patient.systolic_bp < self.threshold:
            return RuleResult(
                rule_id="LOW_SYSTOLIC_BP",
                message=(
                    "Systolic blood pressure is below "
                    "the configured threshold."
                ),
                severity="high"
            )

        return None
