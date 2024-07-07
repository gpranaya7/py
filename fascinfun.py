def fascin(num,res=''):
    for n in range (1,4,1):
        res+=str(n*num)
    print(type(res))
    for val in range(1,10,1):
        if str(val) not in res:
            return "not fascinating"
            
    else:
        return "fascinating"
num=219
print(fascin(num))