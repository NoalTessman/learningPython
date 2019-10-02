for x in range(1, 16):
    number = str(x)
    if x%5 == 0: number += "Buzz"
    if x%3 == 0: number += "Fizz"
    print(number)