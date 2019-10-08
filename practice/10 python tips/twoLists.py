names = ["donavan","rudy","mitchell"]
heroes = ["spiderman","Tall Man", "Spiderman2"]
Universe = ["NBA","MArvel","DC"]
for hero, name, universe in zip(names,heroes,Universe):
    print(f"{name} is actually {hero} from {universe}")
#Zip function, allows you to interate over two lists at once. 
for three in zip(names,heroes,Universe):
    print(three)