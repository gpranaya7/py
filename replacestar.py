str2=''
str1='how are you'
for ch in str1:
    if ch in'aeiouAEIOU':
        str2+='*'
    else:
        str2+=ch
print(str2)
