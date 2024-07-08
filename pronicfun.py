def pronic(num,val=0):
    for n in range(1,num//2+1):
        mul=val*n
        val+=1
        if mul==num:
            return "pronic"
    else:
        return "not pronic"
num=13
print(pronic(num))
