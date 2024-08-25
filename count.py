lccount=0
uccount=0
vowcount=0
concount=0
spch=0
digit=0
s="We Will Learn All Skills 100%"

for ch in s:
    if 'a'<=ch<='z':
        lccount+=1
    elif 'A'<=ch<='Z':
        uccount+=1
        
    if not ('a'<=ch<='z' or
            'A'<=ch<='Z' or '0'<=ch<='9'):
        spch+=1
    if '0'<=ch<='9':
        digit+=1
    
    if  ('a'<=ch<='z' or 'A'<=ch<='Z')  and ch  not in  'aeiouAEIOU':
        concount+=1
    if ch in'aeiouAEIOU' :
        vowcount+=1
print(lccount,uccount,vowcount,concount,spch,digit)