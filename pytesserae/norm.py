"""Normalization functions

Given a word form, we would like to process it into a canonical form against
which we can compare equivalently with other words that have slightly different
forms.  For example, "Ab" and "ab" should match, despite capitalization
differences.

"""
import regex as re
import unicodedata


DIGITS = re.compile(r'\d')
NONWORDS = re.compile(r'\W')
GRAVE = re.compile(r'\u0300')
SIGMA = re.compile(r'σ\b')


def normalize_latin(raw_word):
    """Normalizes a token according to Latin normalization rules

    Parameters
    ----------
    raw_word : str
        A token extracted from a raw text

    Returns
    -------
    str
        The Latin-normalized token

    Examples
    --------
    >>> normalize_latin('Juvat')
    'iuuat'

    """
    nfkd = unicodedata.normalize('NFKD', raw_word)
    lowercased = nfkd.lower()
    no_digits = DIGITS.sub('', lowercased)
    j_to_i = re.sub('j', 'i', no_digits)
    v_to_u = re.sub('v', 'u', j_to_i)
    return NONWORDS.sub('', v_to_u)

def normalize_greek(raw_word):
    """Normalizes a token according to Greek normalization rules

    Parameters
    ----------
    raw_word : str
        A token extracted from a raw text

    Returns
    -------
    str
        The Greek-normalized token

    Examples
    --------
    >>> normalize_greek('σεμνοὺσ')
    'σεμνούς'

    """
    nfkd = unicodedata.normalize('NFKD', raw_word)
    lowercased = nfkd.lower()
    no_digits = DIGITS.sub('', lowercased)
    accented = GRAVE.sub('\u0301', no_digits)
    sigmas = SIGMA.sub('ς', accented)
    return NONWORDS.sub('', sigmas)
