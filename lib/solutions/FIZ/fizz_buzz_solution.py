# noinspection PyUnusedLocal
def fizz_buzz(number):
    if (number%3==0 or '3' in str(number)) and (number%5 == 0 or '5' in str(number)) and (number % 2 == 0):
        return "fizz buzz deluxe"
    elif (number%3==0 or '3' in str(number)) and (number%5 == 0 or '5' in str(number)) and (number % 2 != 0):
        return "fizz buzz fake deluxe"
    elif (number%3==0 and '3' in str(number)) and (number % 2 == 0):
        return "fizz deluxe"
    elif (number%3==0 and '3' in str(number)) and (number % 2 != 0):
        return "fizz fake deluxe"
    elif (number%5 == 0 and '5' in str(number)) and (number % 2 == 0):
        return "buzz deluxe"
    elif (number%5 == 0 and '5' in str(number)) and (number % 2 != 0):
        return "buzz fake deluxe"
    elif (number%3==0 or '3' in str(number)) and (number%5 == 0 or '5' in str(number)):
        return "fizz buzz"
    elif (number%5 == 0 or '5' in str(number)):
        return "buzz"
    elif (number%3==0 or '3' in str(number)):
        return "fizz"
    else:
        return number
