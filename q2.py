__author__ = "Yun Sion"


# Github = https://github.com/Sion-Yun/FIT3155_A1


def z_algorithm(txt: str, pat: str) -> [int]:
    """
    1. Implement the Z-algorithm. Your code should accept a string as input
    and return the Z-values for the string. (Done)
    2. Implement the Z-algorithm based exact pattern matching discussed in
    lectures. Your code should accept a text and a pattern as inputs and
    return (Done)

    Function and approach

    time complexity:
        O(m + n), for m being the length of pattern and n being the length of text.
    space complexity:
        O(n), for n being the length of text.

    :argument:
        txt (str): The text to match.
        pat (str): The pattern to match.
    :return: z_arr: array of all positions in the text where the pattern matches exactly
    """

    z_str = pat + "$" + txt  # input string
    n = len(z_str)  # input string length
    z_arr = [0] * n  # Z-array
    l, r, k = 0, 0, 0  # left right boundary
    out = []  # output array

    """
    Finding the Z-values
    
        What is Z-values?
        - The set of values Z_i
        - Z_i = the length of the longest substring, starting at [i] of string, that matches its prefix.    
    """

    for i in range(1, n):
        # Case 1
        if i > r:
            l, r = i, i
            while r < n and z_str[r - l] == z_str[r]:
                r += 1
            z_arr[i] = r - l
            r -= 1

        # Case 2
        else:
            k = i - l
            # Case 2a
            if z_arr[k] < r - i + 1:
                z_arr[i] = z_arr[k]
            # Case 2b
            else:
                l = i
                while r < n and z_str[r - l] == z_str[r]:
                    r += 1
                z_arr[i] = r - l
                r -= 1

    # all occurrences of the pattern in text
    for i in range(n):
        if z_arr[i] == len(pat):
            out.append(i - len(pat) - 1)

    return out


if __name__ == '__main__':
    # TODO - open file
    # f = open("demofile.txt")

    txt = 'ababcabc'
    pat = 'ab'
    print("pattern found at index", z_algorithm(txt, pat))
