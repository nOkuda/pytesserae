"""Normalization functions

Given a word form, we would like to process it into a canonical form against
which we can compare equivalently with other words that have slightly different
forms.  For example, "Ab" and "ab" should match, despite capitlization
differences.
"""
import re
import unicodedata


DIGITS = re.compile(r'\d')
NONWORDS = re.compile(r'\W')


def normalize_latin(raw_word):
    """Normalizes Latin word"""
    nfkd = unicodedata.normalize('NFKD', raw_word)
    lowercased = nfkd.lower()
    no_digits = DIGITS.sub('', lowercased)
    j_to_i = re.sub('j', 'i', no_digits)
    v_to_u = re.sub('v', 'u', j_to_i)
    return NONWORDS.sub('', v_to_u)
