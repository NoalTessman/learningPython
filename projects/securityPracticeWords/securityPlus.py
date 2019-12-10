import csv

words = csv.writer(open("keyWords.txt","a"), delimiter = ",", lineterminator = "\n")
counter = 0
x = 1
while x == 1:
    newWord = input("Next word pls: ")
    counter += 1
    words.writerow([newWord])
