"""Tests for ensuring that functions in pytesserae.score work properly"""
import pytesserae.score as score


EPSILON = 1e-6


def test_vanilla_normal():
    """Tries out vanilla under normal circumstances"""
    # TODO:  make a real example
    matching_terms = {'hoc', 'illud'}
    source_distance = 5
    target_distance = 6
    source_size = 1643
    target_size = 1788
    source_counts = {'hoc': 73, 'illud': 98}
    target_counts = {'hoc': 65, 'illud': 99}
    expected = 2.04287720584
    assert (
        score.vanilla(
            matching_terms, source_distance, target_distance, source_size,
            target_size, source_counts, target_counts
        ) - expected < EPSILON
    )
