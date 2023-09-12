list=[(1,2,3),(4,5),(6,1),(2,9)]
temp=[]
for i in list:
    temp.append(i[-1])
temp.sort()
final=[]
for i in temp:
    for j in list:
        if i == j[-1]:
            final.append(j)
print(final)
    


    