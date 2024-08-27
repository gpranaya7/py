n=4
for line in range(0,n):
    for st in range(0,n):
        if line==0 or line==n-1:
            print('*',end='')
        else:
            if st==0 or st==n-1:
                print('*',end='')
            else:
                print(' ',end='')
    print()