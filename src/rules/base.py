from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Literal

from models.patient import Patient

Severity = Literal["low", "medium", "high"]

@dataclass
class RuleResult:
    rule_id: str
    message: str
    severity: Severity

class ClinicalRule(ABC):
    @abstractmethod
    def evaluate(self, patient: Patient) -> RuleResult | None:
        pass