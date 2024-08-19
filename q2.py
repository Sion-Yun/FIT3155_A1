__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1


def z_algorithm(txt: str, pat: str) -> [int]:
    """
    1. Implement the Z-algorithm. Your code should accept a string as input
    and return the Z-values for the string. (Done)
    2. Implement the Z-algorithm based exact pattern matching discussed in
    lectures. Your code should accept a text and a pattern as inputs and
    return (Done)

    TODO -  Function and approach

    time complexity:
        O(m + n), for m being the length of pattern and n being the length of text.
    space complexity:
        O(m + n), for m being the length of pattern and n being the length of text.

    :argument:
        txt (str): The text to match.
        pat (str): The pattern to match.
    :return: z_arr: array of all positions in the text where the pattern matches exactly
    """

    z_str = pat + "$" + txt  # combined string with terminal($)
    n = len(z_str)  # length of the combined string
    z_arr = [0] * n  # array to store Z-values
    l, r, k = 0, 0, 0  # left boundary, right boundary, and position of Z-box
    out = []  # output list for pattern match occurrences

    """
    Computing the Z-values
        - The set of values Z_i
        - Z_i = the length of the longest substring, starting at [i] of string, that matches its prefix.    
    """
    for k in range(1, n):
        # Case 1: k is outside the rightmost Z-box
        if k > r:
            l, r = k, k
            while r < n and z_str[r - l] == z_str[r]:  # explicit comparison
                r += 1
            z_arr[k] = r - l  # updating z-value
            r -= 1  # updating right boundary

        # Case 2: k is inside the rightmost Z-box
        else:
            # Case 2a: Z_k-l+1 box does not extend to the end of the prefix that matches Z_l box
            if z_arr[k - l] < r - k + 1:
                z_arr[k] = z_arr[k - l]  # using previous z-value; r and l remains the same

            # Case 2b: Z_k-l+1 box extends over the prefix that matches Z_l box
            else:
                l = k  # updating left boundary
                while r < n and z_str[r - l] == z_str[r]:  # explicit comparison
                    r += 1
                z_arr[k] = r - l  # updating z-value
                r -= 1   # updating right boundary

    """
    Finding all occurrences of the pattern in text
    """
    for i in range(n):
        if z_arr[i] == len(pat):
            out.append(i - len(pat) - 1)  # adjusting pos with the length of pattern and separator
    return out


if __name__ == '__main__':
    # TODO - open file
    # f = open("demofile.txt")

    txt = 'ababcabc'
    pat = 'bc'
    print("pattern found at index", z_algorithm(txt, pat))
