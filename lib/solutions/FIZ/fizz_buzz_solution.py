# noinspection PyUnusedLocal
import collections

def same_dig(number):	
    try:
        countOfWords = collections.Counter(str(number))
        result = [countOfWords[i] for i in countOfWords if countOfWords[i]>1]
        if len(str(number))==result[0]:
            return True
        else:
            return False
    except:
        return False
        

def fizz_buzz(number):
    if (number%3==0 or '3' in str(number)) and (number%5 == 0 or '5' in str(number)) and (number>10 and same_dig(number)==True):
        return "fizz buzz deluxe"
    elif (number>10 and same_dig(number)==True):
         return "deluxe"
    elif (number%3==0 or '3' in str(number)) and (number%5 == 0 or '5' in str(number)):
        return "fizz buzz"
    elif (number%5 == 0 or '5' in str(number)):
        return "buzz"
    elif (number%3==0 or '3' in str(number)):
        return "fizz"
    else:
        return number
