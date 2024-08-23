__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1

import sys


def boyer_more(txt: str, pat:str) -> [int]:
    """
    1. Implement Boyer-Moore’s algorithm for pattern matching. Your script
    accepts files containing the text and pattern as inputs, and outputs

    Function and approach

    time complexity:
    space complexity:

    :argument:
        txt (str): The text to match.
        pat (str): The pattern to match.
    :return: the positions of all instances of the pattern observed in that text.
    """
    pass


if __name__ == '__main__':
    # TODO - open file
    # txt_file = open(sys.argv[1], "r")
    # pat_file = open(sys.argv[2], "r")

    txt = 'ababcabc'
    pat = 'ab'
    print(boyer_more(txt, pat))
