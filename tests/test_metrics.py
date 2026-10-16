
import pytest

from metrics import calculate_metrics


def test_perfect_predictions():
    result = calculate_metrics(
        [True, True, False, False],
        [True, True, False, False],
    )

    assert result.true_positives == 2
    assert result.true_negatives == 2
    assert result.false_positives == 0
    assert result.false_negatives == 0
    assert result.precision == 1.0
    assert result.recall == 1.0


def test_missed_alert():
    result = calculate_metrics(
        [True, True, False],
        [True, False, False],
    )

    assert result.true_positives == 1
    assert result.false_negatives == 1
    assert result.recall == 0.5


def test_unexpected_alert():
    result = calculate_metrics(
        [True, False],
        [True, True],
    )

    assert result.false_positives == 1
    assert result.precision == 0.5


def test_mismatched_input_lengths():
    with pytest.raises(ValueError):
        calculate_metrics([True], [True, False])
