"""Lemmatization functions

Given a word form, we would like to know its possible lemmata.
"""
import gzip
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
    {str: {str: bool}}
        A mapping of word forms to possible lemmata
    """
    with gzip.open(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            language+'.lemma.json.gz'), 'rb') as ifh:
        return json.loads(ifh.read().decode('utf-8'))


_LATIN_LOOKUP = _get_data('latin')
_GREEK_LOOKUP = _get_data('greek')


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
    '[iuuo]'
    """
    normed = pytesserae.norm.normalize_latin(raw_word)
    if normed in _LATIN_LOOKUP:
        return [w for w in _LATIN_LOOKUP[normed]]
    return []


def lemmatize_greek(raw_word):
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
    >>> lemmatize_greek('πέμψεις')
    '[πέμπω, πέμψις]'
    """
    normed = pytesserae.norm.normalize_greek(raw_word)
    if normed in _GREEK_LOOKUP:
        return [w for w in _GREEK_LOOKUP[normed]]
    return []
