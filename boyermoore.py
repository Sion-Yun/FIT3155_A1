__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1

import sys

ALPHABET_SIZE = 256


def z_algo(txt) -> [int]:
    n = len(txt)  # input string
    z = [0] * n  # Z-array
    l, r, k = 0, 0, 0  # left right boundary

    for i in range (1, n):
        # Case 1
        if i > r:
            l, r = i, i
            while r < n and txt[r - l] == txt[r]:
                r += 1
            z[i] = r - l
            r -= 1

        # Case 2
        else:
            k = i - l
            # Case 2a
            if z[k] < r - i + 1:
                z[i] = z[k]
            # Case 2b
            else:
                l = i
                while r < n and txt[r - l] == txt[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

def bad_char(pat):
    pass

def good_suffix(pat):
    pass

def matched_prefix(pat):
    pass


def boyer_moore(txt: str, pat:str) -> [int]:
    """
    Function and approach

    time complexity:
    space complexity:

    :argument:
        txt (str): The text to match.
        pat (str): The pattern to match.
    :return: the positions of all instances of the pattern observed in that text.
    """
    # TODO - scan right to left + galil's optimisation
    # TODO - bad character, good suffix, matched prefix
    pass


if __name__ == '__main__':
    # TODO - open file
    # txt_file = open(sys.argv[1], "r")
    # pat_file = open(sys.argv[2], "r")

    txt = 'ababcabc'
    pat = 'ab'
    # print(boyer_moore(txt, pat))
