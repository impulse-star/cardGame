import sys


if not sys.prefix != sys.base_prefix:
    print("Error, program started with non virtual environment python." +
          "please create a virtual environment first.")
    exit(1)


def main():
    import gameServerAPI
    gameServerAPI.run()
    print('Program Started')


if __name__ == '__main__':
    main()
