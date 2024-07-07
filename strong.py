def strong(num,sum=0):
    while num!=0:
        res=1
        rem=num%10
        for fa in range (rem,0,-1):
            res*=fa
        sum+=res
        num//=10
    return sum
num=40587
print("strong "if strong(num)==num else "not strong")
