"""Lemmatization dictionary generation

Generates lemmatization data

"""
import gzip
import json
import os

import pytesserae.norm


def _generate_lookup(csv_path, normalizer):
    """Generates lookup dictionary as JSON"""
    result = {}
    with open(csv_path) as ifh:
        for line in ifh:
            entries = line.split(',')
            if len(entries) < 3:
                continue
            morphed = normalizer(entries[0])
            lemma = normalizer(entries[2])
            if morphed and lemma:
                if morphed in result:
                    result[morphed][lemma] = True
                else:
                    result[morphed] = {lemma: True}
    return result


def _run():
    """Generates lemma dictionary file"""
    drop_point = os.path.abspath(os.path.join(
        os.path.dirname(os.path.realpath(__file__)), '..', 'pytesserae'))
    latin_lookup = _generate_lookup(
        'la.lexicon.csv',
        pytesserae.norm.normalize_latin,
    )
    with gzip.open(os.path.join(
            drop_point, 'latin.lemma.json.gz'), 'wb') as ofh:
        ofh.write(json.dumps(latin_lookup).encode('utf-8'))
    greek_lookup = _generate_lookup(
        'grc.lexicon.csv',
        pytesserae.norm.normalize_greek,
    )
    with gzip.open(os.path.join(
            drop_point, 'greek.lemma.json.gz'), 'wb') as ofh:
        ofh.write(json.dumps(greek_lookup).encode('utf-8'))


if __name__ == '__main__':
    _run()
