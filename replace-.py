res=''
s='hello world'
for ch in s:
    if ch not in res:
        res+=ch
    else:
        res+='-'
print(res)