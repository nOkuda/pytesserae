"""Tests for ensuring that functions in pytesserae.score work properly"""
import numpy as np

import pytesserae.score as score


def test_vanilla_normal():
    """Tries out vanilla under normal circumstances"""
    # TODO:  make a real example
    hoc = []
    illud = []
    counts = {}
    expected = [5.789]
    assert np.allclose([score.vanilla(hoc, illud, counts)], expected)
