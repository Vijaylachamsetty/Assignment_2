data=int(input("enter number of iterations to built list:"))
list=[]
for i in range(data):
    tup=()
    for j in range(2):
        num=int(input("enter elemts :"))
        tup=tup+(num,)
    list.append(tup)
print("Unsorteed List\n",list)       
temp=[]
for i in list:
    temp.append(i[-1])
temp.sort()
final=[]
for i in temp:
    for j in list:
        if i == j[-1]:
            final.append(j)
print("Sorted List\n",final)
#sample ouput
#[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#sample input
#[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

    


    