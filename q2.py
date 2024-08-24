__author__ = "Yun Sion"
# Github = https://github.com/Sion-Yun/FIT3155_A1
import sys

cumLen, segmentLen = 0, 0
currentSegZ = []
previousSegZ = []
segmentsArr = []
noMatch = False

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

# TODO - make class...
def extract_substrings(pat: str):
    """
    Returns a list of substrings from the input pat that are separated by the '!' character.

    time complexity:
        O(m), for m being the length of input pat.
    space complexity:
        O(m), for m being the length of input pat.

    :param pat: input pat
    :return sliced: an array of slicers between the text and '!' in pat
    """
    m = len(pat)
    substrings = []  # array of the substrings
    sub = ""  # the substring
    flag = True  # are we adding a substring?

    for i in range(m):
        if not pat[i] == '!':
            if flag:
                sub += pat[i]
            else:
                substrings.append(sub)
                sub = pat[i]
                flag = True
        else:
            if flag and sub:
                substrings.append(sub)
                flag = False
                substring = ""

    # append the last substring if any
    if flag and sub:
        substrings.append(sub)

    return substrings


def merge_substrings(txt):
    """
    Merges the extracted substrings (characters) with the length of new z_algo segments.

    time complexity:
        O(n), for n being the length of text.
    space complexity:
        ???
    :param txt:
    """
    global cumLen, segmentLen, currentSegZ, previousSegZ, noMatch
    n = len(txt)
    arr = [0] * n
    k = cumLen + segmentLen  # represents the max length matched after merge
    flag = False

    # TODO - clean later
    for i in range(n):
        if i + k > n:  # stop looping if the remaining is < length after merged
            break

        if previousSegZ[i] == cumLen:
            if currentSegZ[i + cumLen + segmentLen + 1] == segmentLen:
                flag = True
                arr[i] = k

    # a no match found pointer to stop comparing further segments
    if not flag:
        noMatch = True

    previousSegZ = arr  # make this as previous segment of Z

# Function that merges previous processed zarray to length of '?'
# O(n) - n is len(txt)
def merge_wildcard(txt):
    """
    Merges the extracted substrings with the length of new z_algo segments.

    time complexity:
        O(n), for n being the length of text.
    space complexity:
        O(n), for n being the length of text.
    :param txt:
    """
    global cumLen, mergeLen, previousSegZ
    n = len(txt)
    arr = [0] * n
    k = cumLen - mergeLen  # represents the max length matched after merge

    # TODO - later
    # this handle the case when first segment is characters segment where the array is not in
    # size of n, so when merging, it needs a shift of s
    s = 0
    if len(previousSegZ) > n:
        s = len(previousSegZ) - n

    for i in range(s, n):
        if i - s + k > n:  # stop looping if the remaining is < length after merged
            break

        if previousSegZ[i] == cumLen:  # update wanted length
            arr[i - s] = k

    previousSegZ = arr  # make this as previous segment of Z

# Main function to do the matching
# O(k(n+m/k)) - k is total number of segments, n is len(txt), m is len(pat)
def match(txt):
    global cumLen, segmentLen, currentSegZ, previousSegZ, noMatch
    n = len(txt)

    for i in range(len(segmentsArr)):
        if noMatch:    # stop matching further segments, if previous segment hasn't found a match
            break

        if isinstance(segmentsArr[i], str):    # when segment is characters
            x = segmentsArr[i] + "$" + txt
            segmentLen = len(segmentsArr[i])

            if not i == 0:
                currentSegZ = z_algo(x)
                merge_substrings(txt)
            else:
                previousSegZ = z_algo(x)

            cumLen += segmentLen
        else:   # when segment is '?'
            if not i == 0:
                mergeLen = segmentsArr[i]
                merge_wildcard(txt)
            else:
                previousSegZ = [-segmentsArr[0]] * n
            cumLen += -segmentsArr[i]





if __name__ == '__main__':
    # txt_file = open(sys.argv[1], "r")
    # pat_file = open(sys.argv[2], "r")

    # print("pattern found at index", z_algorithm(txt_file.read(), pat_file.read()))
    pass


