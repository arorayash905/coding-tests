A= input()
L, R, X, Y = A.split(" ")
L = int(L)
R = int(R)
X=int(X)
Y=int(Y)


P = 0

for i in range (L, R+1, 1):
    #print("i : ", i)
    y = 0
    while (i!=0):

        if (i%10==X):

            y+=1
        i = i/10
        #print("y : ",y)
        i = int(i)
    if (y==Y):

        P += 1
        #print("P : ", P)

print(P)
