# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.


def check_permutation_counting(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l2 > l1:
        s2, s1 = s1, s2
        l2,l1 = l1,l2
    if l1 - l2 > 1:
        return False

    df = 0
    flag = False
    i = 0
    while i < l2:
        if s1[i+df] == s2[i]:
            pass
        else:
            if flag:
                return False
            else:
                flag = True
                df += l1-l2
                if df:
                    continue
        i+= 1
    return True

if __name__ == '__main__':
    print("OneAway")

    check = [(("abc", "cba"), False),
             (("kalamaro", "kalamarro"), True),
             (("CTCI is not very nice", "random word"), False),
             (("MrJockTVquizPhDbagsfewlynx.", "MrJockTVquizPhDbagsfewlynx."), True),
             (("LeatherDucke","LeatherDucker"),True),
             (("pale","ple"),True),
             (("pale","bale"), True),
             (("pale","bake"), False),
             (("128321","askdmas"), False),
             ]


    for i in check:
        try:
            assert (check_permutation_counting(*i[0]) == i[1])
        except AssertionError:
            print(i)