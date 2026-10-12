from models.patient import Patient
from rules.base import ClinicalRule, RuleResult

class DecisionEngine: 
    def __init__(self, rules:list[ClinicalRule]):
        self.rules = rules

    def evaluate(self, patient:Patient) -> list[RuleResult]:
        results = []

        for rule in self.rules:
            result = rule.evaluate(patient)


            if result is not None:
                results.append(result)

        return results
        