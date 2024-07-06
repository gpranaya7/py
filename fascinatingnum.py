num=218
val=1
res=''
while val!=4:
    res+=str(num*val)
    val+=1
for mul in range(1,10):
    if str(mul) not in res:
        print('not fascinating')
        break
else:
    print('fascinating')