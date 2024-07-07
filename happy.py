def happy(num):
    while num>9:
        res=0
        while num!=0:            
            rem=num%10
            res+=rem**2           
            num//=10
        num=res
    return num
num=23
print("happy" if happy(num)==1 or happy(num)==7 else "not happy")