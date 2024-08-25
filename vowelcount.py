count=0
s='mock interview'
for ch in s:
    if ch in 'aeiouAEIOU':
        count+=1
print(count)