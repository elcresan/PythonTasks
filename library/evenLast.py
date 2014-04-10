'''You are given an array of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...) then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.
For an empty array, the result will always be (zero).
Hints: This task can be solved using Lists indexes, Slices and Built-in Function "sum".
Input: A list of integers.
Output: The number as an integer.
'''

def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    leng = len(array)
    arr = array[0::2]
    x = 0
    if leng > 0:
        for y in arr:
            x += y
        x *= array[leng-1]
    else:
        x = 0   
    return x

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "Empty"