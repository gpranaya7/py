s='mmanamm'
s_=''
for ele in range(len(s)-1,-1,-1):
    s_+=s[ele]
if s_==s:
    print('palindrome')
else:
    print('not palindrome')