"""A template Python file for convenience"""
import argparse


def _parse_args():
    """Parses command line arguments"""
    parser = argparse.ArgumentParser(description='Template file')
    parser.add_argument(
        'required',
        help='an example required argument')
    return parser.parse_args()


def _run():
    """Displays input command line arguments"""
    args = _parse_args()
    print('Required argument value:', args.required)


if __name__ == '__main__':
    _run()
