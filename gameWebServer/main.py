import sys


if not sys.prefix != sys.base_prefix:
    exit(1)


def main():
    print('Hello world')


if __name__ == 'main':
    main()
