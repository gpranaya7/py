
list=[3,4,1,7,2,12,8,6,9,11]
odlist=[]
evenlist=[]
list2=[]
for n in list:
    if n%2==0:
        evenlist.append(n)
    else:
        odlist.append(n)
odlist.sort()
evenlist.sort()
list2.extend(odlist)
list2.extend(evenlist)
print(list2)

        
