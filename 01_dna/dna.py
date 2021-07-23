#!/usr/bin/env python3
"""
Author : biotuxi3 <biotuxi3@localhost>
Date   : 2021-07-22
Purpose: Tetranucleotide frequency
"""

import argparse
import os
from typing import NamedTuple


# --------------------------------------------------
class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:

    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna',
                        metavar='DNA',
                        help='Input DNA sequence')

    args = parser.parse_args()

    """ For file inputs """
    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    # print(f'positional = "{pos_arg}"')
    print(args.dna)


# --------------------------------------------------
if __name__ == '__main__':
    main()
