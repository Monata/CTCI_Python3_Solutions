# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


def check_permutation(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))


def check_permutation_counting(s1, s2):
    if len(s1) != len(s2):
        return False
    counts = {}
    for i in s1:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1

    for i in s2:
        if i in counts:
            counts[i] -= 1
        else:
            return False

    for i in counts.values():
        if i != 0:
            return False
    return True


if __name__ == "__main__":
    print("CheckPermutation")
    check = [(("abc", "cba"), True),
             (("kalamaro", "kalamarro"), False),
             (("CTCI is not very nice", "random word"), False),
             (("MrJockTVquizPhDbagsfewlynx.", "MrJockTVquizPhDbagsfewlynx."), True)]

    for i in check:
        assert (check_permutation(*i[0]) == i[1])
        assert (check_permutation_counting(*i[0]) == i[1])
