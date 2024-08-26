__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1

import sys

ALPHABET_SIZE = 256


def z_algo(txt: str) -> [int]:
    """
    Z-algorithm.

    time complexity:
        O(n), for n being the length of text.
    space complexity:
        O(n), for n being the length of text.

    :argument:
        txt (str): The text to find z-values.
    :return: z_arr: array of all z-values.
    """
    n = len(txt)  # input string
    z = [0] * n  # array to store Z-values
    l, r, k = 0, 0, 0  # left boundary, right boundary, and position of Z-box

    """
    Computing the Z-values
        - The set of values Z_i
        - Z_i = the length of the longest substring, starting at [i] of string, that matches its prefix.    
    """
    for i in range(1, n):
        # Case 1: k is outside the rightmost Z-box
        if i > r:
            l, r = i, i
            while r < n and txt[r - l] == txt[r]:  # explicit comparison
                r += 1
            z[i] = r - l
            r -= 1

        # Case 2: k is inside the rightmost Z-box
        else:
            # Case 2a: Z_k-l+1 box does not extend to the end of the prefix that matches Z_l box
            k = i - l
            # Case 2a
            if z[k] < r - i + 1:
                z[i] = z[k]

            # Case 2b: Z_k-l+1 box extends over the prefix that matches Z_l box
            else:
                l = i
                while r < n and txt[r - l] == txt[r]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z  # return all z-values

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
    # python q1.py <text filename> <pattern filename>
    txt_file = open(sys.argv[1], "r")
    pat_file = open(sys.argv[2], "r")

    boyer_moore(txt_file.read(), pat_file.read())
