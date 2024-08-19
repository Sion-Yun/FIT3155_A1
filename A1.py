def z_algorithm(txt: str, pat: str) -> [int]:
    """
    1. Implement the Z-algorithm. Your code should accept a string as input
    and return the Z-values for the string.
    2. Implement the Z-algorithm based exact pattern matching discussed in
    lectures. Your code should accept a text and a pattern as inputs and
    return

    :return: all positions in the text where the pattern matches exactly
    """
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


# TODO - accept file or string?
def boyer_more(txt: str, pat:str) -> [int]:
    """
    1. Implement Boyer-Moore’s algorithm for pattern matching. Your script
    accepts files containing the text and pattern as inputs, and outputs

    :return: the positions of all instances of the pattern observed in that text.
    """

    pass


if __name__ == '__main__':
    # TODO - open file
    # f = open("demofile.txt")

    txt = 'ababcabc'
    pat = 'pattern'
    print(z_algorithm(txt, pat))