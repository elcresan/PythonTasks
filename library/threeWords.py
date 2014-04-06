'''
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession.
Hints: You can easily solve this task with these useful functions: str.split, str.isalpha and str.isdigit.
Input: A string with words.
Output: True or False, a boolean.
Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < |words| < 100 (This is a simple task).
'''

def checkio(words):
    
    arr = words.split(' ')
    n = 0
    if len(arr) == 1:
        return False
    for x in arr:
        if x.isalpha():
            n +=1
            if n == 3:
                return True
        else:
            n = 0

    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"