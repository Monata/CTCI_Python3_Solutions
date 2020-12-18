# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient
# space at the end to hold the additional characters, and that you are given the "true" length of the string.

def urlify(inp):
    return "%20".join(filter(lambda x: x != "",inp.split(" ")))

check = [("Mr John Smith   ", "Mr%20John%20Smith"),("pan cakes  ","pan%20cakes")]

for i in check:
    assert (urlify(i[0]) == i[1])
