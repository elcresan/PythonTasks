'''You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
Hints: This task can be solved with a simple conversion from int to str and versus. Read more about built-in types here.
Input: A positive integer.
Output: The product of the digits as an integer.
'''

def checkio(number):
    num = 1
    arr = str(number)
    for x in arr:
        if x != '0':
            num *= int(x)

    return num

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1