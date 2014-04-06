#Help Nikola develop a password security check module for Sofia. The password will be considered strong enough if its length #is greater than or equal to 10 symbols, it has at least one digit, as well as containing one uppercase letter and one #lowercase letter in it.
#Input data: A string that is a password (Unicode for python 2.7).
#Output data: The output will be true if the password is safe, a boolean or any data type that can be converted and processed #as a boolean. In the results you will see the converted results.

def checkio(data):
    
    if len(data) < 10:
        return False
    if data.islower():
        return False
    if data.isupper():
        return False
    if data.isdigit():
        return False
    if data.isalpha():
        return False
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"