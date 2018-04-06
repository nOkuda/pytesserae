"""Lemmatization functions

Given a word form, we would like to know its possible lemmata.
"""
import json
import os

import pytesserae.norm


def _get_data(language):
    """Loads data for lemmatization

    Parameters
    ----------
    language : str
        The kind of lemma dictionary to load

    Returns
    -------
    {str: {str}}
        A mapping of word forms to possible lemmata
    """
    with open(os.path.join(
            os.path.realpath(__file__), language+'.lemma.json')) as ifh:
        json.load(ifh)
        # TODO finish implementing
    return {}


_LATIN_LOOKUP = _get_data('latin')


def lemmatize_latin(raw_word):
    """Lemmatizes a token according to Latin lemmatization rules

    Parameters
    ----------
    raw_word : str
        A token extracted from raw text

    Returns
    -------
    [str]
        All possible lemmata for `raw_word`

    Examples
    --------
    >>> lemmatize_latin('Juvat')
    'iuuo'
    """
    normed = pytesserae.norm.normalize_latin(raw_word)
    if normed in _LATIN_LOOKUP:
        return [w for w in _LATIN_LOOKUP[normed]]
    return []
