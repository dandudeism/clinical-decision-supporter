from dataclasses import dataclass
from rules.base import RuleResult

SEVERITY_POINTS = {
    "low":1,
    "medium":2,
    "high":3,
}

@dataclass
class RiskAssessment:
    score: int
    category: str
    triggered_rules: list[str]

def calculate_risk(
    results: list[RuleResult],
) -> RiskAssessment:
    score = sum(
        SEVERITY_POINTS[result.severity]
        for result in results
    )

    if score == 0:
        category = "no_alerts"
    elif score <= 2:
        category = "low"
    elif score <= 4:
        category = "moderate"
    else:
        category = "high"

    return RiskAssessment(
        score=score,
        category=category,
        triggered_rules=[
            result.rule_id for result in results
        ],
    )