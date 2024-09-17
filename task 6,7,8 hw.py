#Author: CMC
#Date: Sept 24
#Title: Task 6,7 and 8

#Task 6:
print("2 + %d = 4"   %2)
print("2 + %d = %d"  %(2, 4))
print("%d + %d = %d" %(2, 2, 4))
print("%d + %d = %d" %(2, 2, 2+2))

#Task 7:
print("%s" %3)
print("%d" %3.14)
print("%f" %3)
# print("%f" %"Hi!")

#Task 8:
msg = "Hi %s. How are you?"
name = "Hal"
print(msg%name)

import math
r = 5
print("Radius: %d, Area: %.2f" %(r, 2*math.pi*r))
