def tech(num,var,res=0):
    num1=int(var[:len(var)//2:])
    num2=int(var[len(var)//2:])
    print(num1)
    print(num2)
    res=(num1+num2)**2
    return res
num=2025
print("tech " if tech(num,var=str(num))==num else "not tech")

