numbers = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine"
}
print("Phone:")
phone_number = list(map(int, input()))
for x in range(len(str(phone_number))):
    print(f"{numbers[phone_number[x]]}")
#My solution that fails after it's all complete
phone = input("Phone: ")
#using the same numbers dictionary
output = ""
for ch in phone:
    output += numbers.get(ch, "!") + " "
print(output)
