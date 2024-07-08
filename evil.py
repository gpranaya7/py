def evil(num,count=0):
    while num!=0:
        rem=num%2
        if rem==1:
            count+=1
        num//=2
    return count
num=10
print('evil' if evil(num)%2==0 else 'odeous')
