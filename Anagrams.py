S1 = input()
S2 = input()
count = 0
SS1 = []
SS2 = []

for s in S1:
    if s == " ":
        continue
    else:    
        SS1.append(s.lower())
for s in S2:
    if s == " ":
        continue
    else: 
        SS2.append(s.lower())


SS1.sort()
SS2.sort()
print("SS1 : ", SS1)
print("SS2 : ", SS2)
if (len(SS1) == len(SS2)):
    for i in range(0, len(SS1)):
        if SS1[i] == SS2[i]:
            count += 1
        else:
            print("No")
    if count == len(SS1):
        print("Yes")
else:
    print("No")
