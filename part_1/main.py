from sys import argv
from sorter import Sorter


def usage():
    print("Usage: python3 main.py DIR_PATH")


def main():
    if len(argv) != 2:
        usage()

    try:
        sorter = Sorter(argv[1])
    except FileNotFoundError as err:
        print(err)
        usage()
        exit(1)

    sorter.sort_it_out()


if __name__ == "__main__":
    main()
