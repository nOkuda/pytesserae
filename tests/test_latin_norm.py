"""Test Latin normalization"""
from pytesserae.norm import normalize_latin


def test_latin_normalization_simple():
    """Tests Latin normalization when nothing should change"""
    word = 'amor'
    expected = 'amor'
    assert(expected == normalize_latin(word))


def test_latin_normalization_lower():
    """Tests Latin normalization when capitalization occurs"""
    word = 'Amor'
    expected = 'amor'
    assert(expected == normalize_latin(word))


def test_latin_normalization_macron():
    """Tests Latin normalization when macron occurs"""
    word = 'linguā'
    expected = 'lingua'
    assert(expected == normalize_latin(word))


def test_latin_normalization_j():
    """Tests Latin normalization when j occurs"""
    word = 'jus'
    expected = 'ius'
    assert(expected == normalize_latin(word))


def test_latin_normalization_v():
    """Tests Latin normalization when v occurs"""
    word = 'verum'
    expected = 'uerum'
    assert(expected == normalize_latin(word))


def test_latin_normalization_jv():
    """Tests Latin normalization when both j and v occur"""
    word = 'juvo'
    expected = 'iuuo'
    assert(expected == normalize_latin(word))


def test_latin_normalization_numbers():
    """Tests Latin normalization when a numeral occurs"""
    word = 'ab2'
    expected = 'ab'
    assert(expected == normalize_latin(word))


def test_latin_normalization_quotes():
    """Tests Latin normalization when quotation marks occur"""
    word = '"deus"'
    expected = 'deus'
    assert(expected == normalize_latin(word))
