#!/usr/bin/env python3
from genDiff.args_parser import get_args
from genDiff.index import genDiff


def main():
    args = get_args()
    print(genDiff(args.first_file, args.second_file))


if __name__ == "__main__":
    main()
