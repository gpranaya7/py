l=[0,1,2,3]
for ind in range(len(l)):
    for ind2 in range(ind,len(l)):
        for ind3 in range(ind,ind2+1):
            print(ind3)
        print('_')
    