N=int(input("N="))
X=int(input("X="))
Y=int(input("Y="))
T=int(input("T="))

ListA=[no for no in range(1,N+1) if no%X==0 ]
ListB=[no for no in range(1,N+1) if no%Y==0 ]
pairs=[]

for i in ListA:
    for j in ListB:
        if i+j==T:
            pairs.append((i,j))
print('ListA =', ListA)
print('ListB =', ListB)
print('T =', pairs)
