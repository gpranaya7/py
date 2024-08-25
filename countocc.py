s='hello'
d={}
for ch in s:
    if ch not in d:
        d[ch]=[s.count(ch)]
print(d)
