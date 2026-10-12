from abc import ABC, abstractmethod
from dataclasses import dataclass

from models.patient import Patient

@dataclass
class RuleResult:
    rule_id: str
    message: str
    severity: str

class ClinicalRule(ABC):
    @abstractmethod
    def evaluate(self, patient: Patient) -> RuleResult | None:
        pass