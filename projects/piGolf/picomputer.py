from __future__ import division
#defining pi using an infinite series
odd, series,pieDone = (3,1,1)

def pi():
    global odd, series, pieDone
    #print(pieDone)
    if series % 2 == 0:pieDone += 1/odd
    else:pieDone -= 1/odd
    #print 1/odd
    series += 1
    odd += 2
    return
piDigit = 10000000
def pie():
    for x in range(piDigit):
        pi()
pie()
py = pieDone*4
print(py)
##Although this calculates pi, computing the digits of pi doesn't make sense for this project when the Math Library exists,
#This does put out pi, but only 11 digits of it Using one of the math infinites I've seen before. The a repeating function (1 - 1/3 + 1/5 -1/7) ad infinitum.
#The more iterations, the more accurate the digits you get.
#For now, these digits are limited to 11 points after the decimal, so I will try using eitehr a txt file containing pi or using Math()
