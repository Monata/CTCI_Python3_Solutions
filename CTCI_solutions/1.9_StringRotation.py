# Assumeyou have a method isSubstringwhich checks if oneword is a substring of another. Given two strings, sl and s2,
# write code to check if s2 is a rotation of sl using only one call to isSubstring
# (e.g., "waterbottle" is a rotation of"erbottlewat")



def string_rotate(s1,s2):
    l = len(s2)
    if len(s1) != len(s2):
        return False
    c = s1[0]
    ind = -1
    while True:
        try:
            ind = s2.index(c,ind+1)
        except ValueError:
            return False
        if s2[ind:] == s1[:l-ind]:
            if s1[l-ind:] == s2[:ind]:
                return True

if __name__ == '__main__':
    print("StringRotation")

    check = [(("abc", "cba"), False),
             (("kalamaro", "kalamarro"), False),
             (("CTCI is not very nice", "random word"), False),
             (("MrJockTVquizPhDbagsfewlynx.", "MrJockTVquizPhDbagsfewlynx."), True),
             (("LeatherDucke","LeatherDucker"),False),
             (("pale","ple"),False),
             (("pale","bale"), False),
             (("pale","bake"), False),
             (("128321","askdmas"), False),
             (("waterbottle","erbottlewat"),True),
             (("wawa","awaw"),True),
             (("echoesofthedistant","distantechoesofthe"),True),
             (("strangerspassinginthestreet","bychancetwoseperateglancesmeet"),False)
             ]


    for i in check:
        try:
            assert (string_rotate(*i[0]) == i[1])
        except AssertionError:
            print("ERROR",i)