__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1

import sys


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

def bad_character(pat: str):
    """
    Creates a bad-character table of all printable ASCII characters.

    Time complexity:
        O(m * d), for m being the length of the pat and d is the number of distinct ASCII characters.
    Space complexity:
        O(m * d), for the bad character table.

    :arg: pat (str): The pattern string.
    :return: bc_table: A list of entries to the last occurrence of each ASCII character.
    """
    bad_char_table = []
    ascii_range = 126 - 33  # using only the printable ASCII characters

    # initialising bad char table (or 2-D array)
    for _ in range(ascii_range):
        row = [-1] * len(pat)
        bad_char_table.append(row)

    # filling up the bad char table
    for i in range(len(pat)):
        char_i = ord(pat[i]) - 33  # index of current char
        bad_char_table[char_i][i] = i  # position of the char in pat

    # updating the table
    for i in range(len(bad_char_table)):
        last_seen = -1
        for j in range(len(bad_char_table[0])):
            if bad_char_table[i][j] != -1:
                last_seen = bad_char_table[i][j]
            else:
                bad_char_table[i][j] = last_seen

    return bad_char_table

def good_suffix_legacy(pat: str):
    """
    *This is not the implementation for A1*
    (This is not the stricter good suffix rule, therefore renamed as legacy for A1.)
    Creates a good suffix table of the pattern.

    Time complexity:
        O(m), for m being the length of the pattern.
    Space complexity:
        O(m), for the good suffix array.


    :arg: pat (str): The pattern string.
    :return: good_suffixes: A list of the good suffix array of the pattern
    """
    m = len(pat)
    good_suffixes = [0] * m  # initialising the good suffix array

    # creating z-suffix array with z_algorithm using the reversed pattern
    z_suffix = z_algo(pat[::-1])[::-1]  # reverse the result of z_algo(reversed_pat)

    # filling the good suffix array
    for p in range(m-1):
        j = m - z_suffix[p] - 1
        if j >= 0:
            good_suffixes[j] = p + 1  # the shift
    return good_suffixes

def matched_prefix(pat: str):
    """
    Creates a matched prefix table of the pattern.

    Time complexity:
        O(m), for m being the length of pattern.
    Space complexity:
        O(m), for the matched prefix list.

    :arg: pat (str): The pattern string.
    :return: mp_array: A list of the matched prefix of the pattern.
    """
    m = len(pat)
    match_prefixes = [0] * m
    z_prefix = z_algo(pat)  # Z-prefix list

    # filling the matched prefix array
    for i in range(m):
        if (z_prefix[m-i-1] + m-i-1) != m and m-i < m:
            match_prefixes[m-i-1] = match_prefixes[m-i]  # copy the prefix if no full match
        else:
            match_prefixes[m-i-1] = z_prefix[m-i-1]  # using the z-prefix

    return match_prefixes

def boyer_moore(txt: str, pat: str):
    """
    The Boyer-Moore string search algorithm.

    Time complexity:
        O(n + m), for n being the length of the text and m being the length of the pattern.
    Space complexity:
        O(m * d), d for the number of ASCII characters, and m for the good suffix and matched prefix arrays.

    :argument:
        txt (str): The text to match.
        pat (str): The pattern to match.
    """
    n = len(txt)
    m = len(pat)
    result = []

    # checking if the inputs are suitable for the boyer-moore algo
    if n < m or n == 0 or m == 0:
        return result

    # preprocessing the pattern
    bc_table = bad_character(pat)  # Bad character table
    # gs_list = good_suffix_legacy(pat)  # Good suffix table (excluded for A1)
    mp_list = matched_prefix(pat)  # Matched prefix table

    shift = 0  # initial shift

    # searching the pat in the txt
    while shift <= n - m:
        j = m - 1  # last char of the pat

        # right-to-left search
        while j >= 0 and pat[j] == txt[shift + j]:
            j -= 1

        # pattern found
        if j < 0:
            result.append(shift)  # append position
            shift += m - mp_list[0] if m > 1 else 1  # shift by m - the matched prefix
        else:
            bad_char = txt[shift + j]

            # bad-char shift
            if ord(bad_char) - 33 >= 0:
                bc_shift = j - bc_table[ord(bad_char) - 33][j]
            else:
                bc_shift = j + 1

            # *stricter* good_suffix shift for A1
            gs_shift = 0
            if j < m - 1:
                # finding the rightmost instance of good suffix followed by the bad character
                for p in range(j + 1, m):
                    # req 1:  pat[p − m + k + 1 . . . p] ≡ pat[k + 1 . . . .m]
                    if pat[p - m + j + 1: p + 1] == pat[j + 1:]:
                        # req 2: pat[p − m + k], is identical to the bad character
                        if p - m + j >= 0 and pat[p - m + j] == bad_char:
                            gs_shift = m - p
                            break

            # shift by the maximum of the bad character and good suffix shifts
            shift += max(bc_shift, gs_shift)

    with open("output_q1.txt", "w+") as f:
        for i in range(len(result)):
            f.write("%d\n" % (result[i] + 1))  # shift + 1 to adjust for 1-based indexing


if __name__ == '__main__':
    # python q1.py <text filename> <pattern filename>
    txt_file = open(sys.argv[1], "r")
    pat_file = open(sys.argv[2], "r")

    boyer_moore(txt_file.read(), pat_file.read())