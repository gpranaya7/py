def binint(num,power=0,res=0):
    while num!=0:
        rem=num%10
        res+=rem*(2**power)
        power+=1
        num//=10
    return res 
num=1110
print(binint(num))
