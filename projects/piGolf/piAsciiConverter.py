pi = open("./pi1000000.txt","r")
piNum = pi.read()
piList = []
piWord = ""
x,y = (0,0)
digit = 999998
while x < digit:
    asci = chr(int(piNum[x] + piNum[x+2] + piNum[x+3]))
    piWord +=asci
    x+=3
print piWord
pi.close()
#I don't believe I'm using the right tools, I can't seem to find any words, just a lot of nonsense. 
def writeToTxt():
    piDoc = open('./piWords.txt', "r+")
    piDoc.write(piWord)
    piDoc.close()