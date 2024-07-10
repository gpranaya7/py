def bin(num,pow=0):
    if num==0:
        return 0
    return (num%10)*(2**pow)+bin(num//10,pow+1)
num=1110
print(bin(num))
