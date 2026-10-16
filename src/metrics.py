
from dataclasses import dataclass


@dataclass
class ClassificationMetrics:
    true_positives: int
    false_positives: int
    false_negatives: int
    true_negatives: int

    @property
    def precision(self) -> float:
        denominator = (
            self.true_positives + self.false_positives
        )
        if denominator == 0:
            return 0.0

        return self.true_positives / denominator

    @property
    def recall(self) -> float:
        denominator = (
            self.true_positives + self.false_negatives
        )
        if denominator == 0:
            return 0.0

        return self.true_positives / denominator


def calculate_metrics(
    expected: list[bool],
    predicted: list[bool],
) -> ClassificationMetrics:
    if len(expected) != len(predicted):
        raise ValueError(
            "Expected and predicted lists must have equal length."
        )

    tp = fp = fn = tn = 0

    for actual, prediction in zip(expected, predicted):
        if actual and prediction:
            tp += 1
        elif not actual and prediction:
            fp += 1
        elif actual and not prediction:
            fn += 1
        else:
            tn += 1

    return ClassificationMetrics(tp, fp, fn, tn)
