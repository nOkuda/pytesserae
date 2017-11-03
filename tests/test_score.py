"""Tests for ensuring that functions in pytesserae.score work properly"""
import pytesserae.score as score


EPSILON = 1e-6


def test_vanilla_normal():
    """Tries out vanilla under normal circumstances"""
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


def test_get_two_lowest():
    """Test _get_two_lowest when there are two matching terms"""
    matching_terms = {'a', 'b'}
    counts = {'a': 20, 'b': 25}
    term1, term2 = score._get_two_lowest(matching_terms, counts)
    assert term1 == 'a' and term2 == 'b'


def test_get_two_lowest_more():
    """Test _get_two_lowest when there are more than two matching terms"""
    matching_terms = {'a', 'b', 'c'}
    counts = {'a': 20, 'b': 25, 'c': 30}
    term1, term2 = score._get_two_lowest(matching_terms, counts)
    assert term1 == 'a' and term2 == 'b'


def test_find_distance():
    """Test find_distance when there are two matching terms"""
    matching_terms = {'a', 'b'}
    chunk = ['a', 'b']
    counts = {'a': 20, 'b': 25}
    distance = score.find_distance(matching_terms, chunk, counts)
    assert distance == 1


def test_find_distance_more():
    """Test find_distance when there are more than two matching terms"""
    matching_terms = {'a', 'b', 'c'}
    chunk = ['a', 'c', 'b']
    counts = {'a': 20, 'b': 25, 'c': 30}
    distance = score.find_distance(matching_terms, chunk, counts)
    assert distance == 2


def test_find_distance_one():
    """Test find_distance when there is one matching term"""
    matching_terms = {'a'}
    chunk = ['a', 'b', 'a']
    counts = {'a': 20, 'b': 25}
    distance = score.find_distance(matching_terms, chunk, counts)
    assert distance == 2
