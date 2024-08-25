s='kayyyakk'
pal=''
for ind in range(0,len(s)):
    if s[ind]==s[(len(s)-1)-ind]:
        pal+=s[ind]
if s==pal:
    print("palindrome")
else:
    print("not palindrome")