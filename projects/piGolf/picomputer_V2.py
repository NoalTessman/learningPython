import math

pi = format(math.pi, '.5000f')
print(pi)
print 0.1+0.1+0.1 == 0.3
#python cannot display integers correctly, nor calculate basic functions.
#That's because base 2 is terrible at displaying large amounts of points after the decimal, 
#all this does is find pi to the 5000nth point after the decimal, but after...not many points, it fails out. 
#I think I may have to find a large text file or something with a large amount of digits of pi