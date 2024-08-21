s="hi hello 3456 7890"
sum=0
for n in s:

    if n in '0123456789':
        if int(n)%2==0:
        
            sum+=int(n)
   
print(sum)
        