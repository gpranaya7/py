
def bin(num,pos=1):
    if  num==0 or num==1:
        return 1*pos
    return (num%2)*pos+bin(num//2,pos*10)
num=14
print(bin(num))