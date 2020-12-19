# : Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).
from random import random

def string_compressor(inp):
    res = []
    c = 1
    for i in range(1,len(inp)):
        if inp[i] != inp[i-1]:
            res.append( inp[i-1] + str(c))
            c = 1
        else:
            c += 1
    res.append(inp[-1] + str(c))
    res = "".join(res)
    if len(res) > len(inp):
        return inp
    return res



if __name__ == "__main__":
    print("StringCompression")
    check = [("aabcccccaaa", "a2b1c5a3"),("a","a"),("aa","a2"),("abbb","a1b3")]

    for i in check:
        assert (string_compressor(i[0]) == i[1])
