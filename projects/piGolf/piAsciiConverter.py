pi = open("./pi1000000.txt","r")
piNum = pi.read()
piList = []
piWord = ""
x,y = (0,0)
digit = 999999
while x < digit:
    if int(piNum[x] + piNum[x+2] + piNum[x+3])< 122:
        asci = chr(int(piNum[x] + piNum[x+2] + piNum[x+3]))
        if ord(asci) >= 65 and ord(asci) <= 89: piWord += asci
        elif ord(asci) >= 97 and ord(asci) <= 122: piWord += asci.upper()
        print (asci)
    x+=3
print piWord
pi.close()
#I don't believe I'm using the right tools, I can't seem to find any words, just a lot of nonsense. 
def writeToTxt():
    piDoc = open('./piWords.txt', "r+")
    piDoc.write(piWord)
    piDoc.close()
writeToTxt()