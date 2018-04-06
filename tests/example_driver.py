import argparse
import test_dictionary as td
import handler

def _parse_args():
    parser = argparse.ArgumentParser(
        description='Find matching terms between two texts')
    parser.add_argument(
        'source',
        help='The starting point for allusion-finding')
    parser.add_argument(
        'target',
        help='The text in which one hopes to find allusions')
    return parser.parse_args()

def _run():
    args = _parse_args()
    source_tokens = handler.word_hoard(args.source)
    target_tokens = handler.word_hoard(args.target)
    for tokens1 in source_tokens:
        for tokens2 in target_tokens:
            matches = td.matchify(tokens1, tokens2)
#            counts = td.countify(tokens1, tokens2)
#            print(counts)
            print(matches)

if __name__ == '__main__':
    _run()
