# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?


def is_unique_no_memory(inp):
    # for each char check if that character exists in the rest of the string n^2
    for i in range(len(inp)):
        for j in range(i + 1, len(inp)):
            if inp[i] == inp[j]:
                return False
    return True


def is_unique(inp):
    # set removes the duplicates
    return len(set(inp)) == len(inp)

def is_unique_no_memory_log_n(inp):
    # for each char check if that character exists in the rest of the string
    # inp.sort() sort the string
    for i in range(1,len(inp)):
        if inp[i] == inp[i-1]:
            return False
    return True


if __name__ == "__main__":
    print("IsUnique")
    check = [("abc", True), ("kalamaro", False), ("CTCI is not very nice", False), ("MrJockTVquizPhDbagsfewlynx.", True)]

    for i in check:
        assert (is_unique_no_memory(i[0]) == i[1])
        # assert (is_unique_no_memory_log_n(i[0]) == i[1])
        assert (is_unique(i[0]) == i[1])
