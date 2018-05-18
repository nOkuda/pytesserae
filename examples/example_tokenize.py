"""Example for using tokenize function"""
import argparse
import pytesserae.handler as handler


def _parse_args():
    parser = argparse.ArgumentParser(
        description='Normalizes and tokenizes a line from a .tess file')
    parser.add_argument(
        'text',
        help='A .tess file')
    return parser.parse_args()


def _run():
    args = _parse_args()
    with open(args.text, 'r') as ifh:
        for line in ifh:
            print(handler.tokenize(line))


if __name__ == '__main__':
    _run()
