'''
For language training our Robots want to learn about suffixes.
In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.
Hints: For this task you should know how to iterate through set types and string data type functions. Read more about set type here and string functions here.
Input: A set of words.
Output: True or False, as a boolean.
'''
def checkio(words_set):

    for x in words_set:
        for i in words_set:           
            if i != x and i.endswith(x):
                return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"
