def arm(num,mod):
    if num==0:
        return 0
    return (num%10)**mod+arm(num//10,mod)
num=372

var=arm(num,len(str(num)))

print('armstrong' if var==num else 'not armstrong')