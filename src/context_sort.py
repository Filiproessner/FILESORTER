import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sorter import sort_files


def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        sys.exit(1)

    sort_files(path)


if __name__ == "__main__":
    main()
