# noinspection PyUnusedLocal
def fizz_buzz(number):
    if (number%3==0 or 3 in number) and (number%5 == 0 or 5 in number):
        return "fizz buzz"
    elif number%5 == 0 or 5 in number:
        return "buzz"
    elif number%3==0 or 3 in number:
        return "fizz"
    else:
        return number

print(fizz_buzz(35))