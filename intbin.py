def bin(num,pos=1,res=0):
    while num!=0:
        rem=num%2
        res+=rem*pos
        pos=pos*10
        num//=2
    return res
num=14
print(bin(num))
