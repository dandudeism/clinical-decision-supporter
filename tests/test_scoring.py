
from rules.base import RuleResult
from scoring import calculate_risk


def test_empty_results_produce_zero_score():
    assessment = calculate_risk([])

    assert assessment.score == 0
    assert assessment.category == "no_alerts"
    assert assessment.triggered_rules == []


def test_high_severity_alert_scores_three_points():
    results = [
        RuleResult(
            rule_id="LOW_SYSTOLIC_BP",
            message="Illustrative test alert",
            severity="high",
        )
    ]

    assessment = calculate_risk(results)

    assert assessment.score == 3
    assert assessment.category == "moderate"


def test_multiple_alerts_are_combined():
    results = [
        RuleResult("RULE_A", "Test alert A", "high"),
        RuleResult("RULE_B", "Test alert B", "medium"),
        RuleResult("RULE_C", "Test alert C", "medium"),
    ]

    assessment = calculate_risk(results)

    assert assessment.score == 7
    assert assessment.category == "high"
    assert len(assessment.triggered_rules) == 3
