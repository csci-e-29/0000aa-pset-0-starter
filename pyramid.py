#!/usr/bin/env python3

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Prints a pyramid of a given height
    E.g. a height 3 pyramid looks like:
    --=--
    -===-
    =====
    :param int rows: total height
    """
    cols = rows * 2 - 1
    for i in range(rows):
        cur_row = ""
        for j in range(cols):
            if abs((cols + 1) / 2 - (j + 1)) <= i:
                cur_row = cur_row + "="
            else:
                cur_row = cur_row + "-"
        print(cur_row)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(int(args.rows))
