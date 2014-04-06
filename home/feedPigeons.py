'''
I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on
(Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds,
the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. 
If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?
'''

def otherSol(number):
    birds = mins = 0
    while number > birds:
        mins += 1
        birds += min(mins, number - birds)
        number -= birds
    return birds

def pigAtMin(num):
    return (num*(num+1))/2

def checkio(number):
    i = min = 1
    while i == 1:
        pig = pigAtMin(min)      
        #not enough portions to feed all the pigeons of this minute        
        if number - pig <= 0:
            # Enough portions to feed new pigeons
            if number > pigAtMin(min-1):
                i = 0
                pig = number
            # Not enough porions to feed new pigeons
            else:
                i = 0
                pig = pigAtMin(min-1)
        # Enough portions to feed all the pigeons from this minute, lets feed more!
        else:
            number -= pig
            min += 1
        
    return pig 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"