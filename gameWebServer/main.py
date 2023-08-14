import sys


if not sys.prefix != sys.base_prefix:
    print("Error, program started with non virtual environment python." +
          "please create a virtual environment first.")
    exit(1)


def main():
    print('Hello world')


if __name__ == '__main__':
    main()
