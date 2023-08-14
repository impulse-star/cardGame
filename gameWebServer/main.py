import sys
import gameServerAPI


if not sys.prefix != sys.base_prefix:
    print("Error, program started with non virtual environment python." +
          "please create a virtual environment first.")
    exit(1)


def main():
    print("Server Coming Online.")
    gameServerAPI.run()
    print('Server Has Shut Down.')


if __name__ == '__main__':
    main()
