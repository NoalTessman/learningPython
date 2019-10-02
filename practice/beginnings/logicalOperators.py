Egg = True
Sandwich = False

if Egg and Sandwich:
    print("wee")
else:
    print(
        'woo'
    )
#And operator, very simple
if Egg or Sandwich:
    print("wee")
else:
    print(
        'woo'
    )
#Or operator
if Egg and not Sandwich:
    print("wee")
else:
    print(
        'woo'
    )
#not operator, really neat, if not one varible then the whole function returns false
temp=25
temp2 = 30
if temp > 30:
    print("it hot")
elif temp <10:
    #elif is the worst one so far for else if statements
    print('it cold')
else:
    print('it temperate')