"""Example of the match function"""
import pytesserae.matcher as matcher


def _run():
    source = ['a', 'b', 'c']
    target = ['b', 'c', 'd']
    print(matcher.match(source, target))


if __name__ == '__main__':
    _run()
