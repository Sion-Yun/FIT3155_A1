__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1
import sys


def z_algo(txt) -> [int]:
    """
    z_algorithm.

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


def extract_substrings(txt: str):
    """
    Returns a list of substrings from the input string that are separated by the '!' character.

    time complexity:
        O(n), for n being the length of input string.
    space complexity:
        O(n), for n being the length of input string.

    :param txt: input string
    :return sliced: an array of slicers between the text and '!' in pat
    """
    # TODO - bit confusing names
    n = len(txt)
    substrings = []  # array of slicers to be returned
    substring = ""  # the current substring
    flag = True  # are we adding a substring?

    for i in range(n):
        if not txt[i] == '!':
            if flag:
                substring += txt[i]
            else:
                substrings.append(substring)
                substring = txt[i]
                flag = True
        else:
            if flag and substring:
                substrings.append(substring)
                flag = False
                substring = ""

    # append the last substring if any
    if flag and substring:
        substrings.append(substring)

    return substrings


if __name__ == '__main__':
    txt_file = open(sys.argv[1], "r")
    pat_file = open(sys.argv[2], "r")

    # print("pattern found at index", z_algorithm(txt_file.read(), pat_file.read()))
