"""Tests for ensuring that functions in pytesserae.score work properly"""
import pytesserae.score as score


EPSILON = 1e-6


def test_vanilla_normal():
    """Tries out vanilla under normal circumstances"""
    # TODO:  make a real example
    matching_terms = {'hoc', 'illud'}
    source_distance = 1
    target_distance = 1
    source_counts = {'hoc': 73, 'illud': 98}
    target_counts = {'hoc': 65, 'illud': 99}
    expected = 1.4191252668389973
    assert (
        score.vanilla(
            matching_terms, source_distance, target_distance, source_counts,
            target_counts
        ) - expected < EPSILON
    )
