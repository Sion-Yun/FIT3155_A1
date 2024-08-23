__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1

import sys


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


def bad_character(pat:str):
    pass


def good_suffix(pat: str):
    pass


def matched_prefix(pat: str):
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

    """
    The following tasks are performed by preprocessing the pattern and assuming a fixed size alphabet and input
    pat[1 . . . m], can be completed in O(m) time:
    • Preprocess the R(x) (Rk(x)) values for the bad character (extended bad character) rule.
    • Preprocess the gs and mp values needed for the good suffix rule.
    """

    """
    Given inputs pat[1 . . . m] and txt[1 . . . m] begin by aligning pat[1 . . . m] with txt[1 . . . m]. The algorithm
    proceeds as follows:
    1. Compare the current alignment in a right-to-left scan, applying Galil’s optimisation to terminate the
    scan prematurely if appropriate.
    2. After the scan has terminated due to a mismatch, or an occurrence of the pattern being found (which
    is output appropriately):
    (a) Use the (extended) bad character rule to determine how many places to the right pat should be
    shifted under txt. Call this amount nbadcharacter.
    (b) Use the good suffix and the matched prefix rules to determine how many places to the right pat
    should be shifted under txt. Call this amount ngoodsuffix.
    3. Shift pat to the right under txt by max(nbadcharacter, ngoodsuffix) places. Return to step 1.
    """

    pass


if __name__ == '__main__':
    # TODO - open file
    # txt_file = open(sys.argv[1], "r")
    # pat_file = open(sys.argv[2], "r")

    txt = 'ababcabc'
    pat = 'ab'
    print(boyer_moore(txt, pat))
