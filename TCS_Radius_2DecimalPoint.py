'''

TCS question 1

***   String Approach  ***
___Algorithm___

'''


import math

r = int(input("Enter Radius : "))
count = 2
if (20<= r <= 30):
    p = math.pi * r * r
    p = str(p)
    for i in p:
        count = count + 1
        if i == '.':
            break
    p = p[:count]
    #p = float(p)
    print(p)
    
else:
    print("Invalid Input Number")
