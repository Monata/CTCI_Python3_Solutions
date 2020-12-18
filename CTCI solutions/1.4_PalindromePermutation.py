# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.


def is_palindrome(inp):
    allowed_chars = [" "]
    odd = False
    for i in set(inp):
        if i in allowed_chars:
            continue
        if inp.count(i) % 2 == 1:
            if odd:
                return False
            else:
                odd = True
    return True


if __name__ == '__main__':

    print("PalindromePermutation")

    check = [("abc", False), ("kalamaro", False),
             ("CTCI is not very nice", False),
             ("MrJockTVquizPhDbagsfewlynx.", False),
             ("taco cat", True),
             ("101101", True),
             ("11111111111122", True)]

    for i in check:
        assert (is_palindrome(i[0]) == i[1])
