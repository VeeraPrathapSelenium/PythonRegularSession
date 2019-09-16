str1='welcometopythontraining'
vowels, consonents=0,0
for x in str1:
    print(x)
    if x in ('a','e', 'i', 'o', 'u'):
        vowels+=1
    else:
        consonents+=1
print(vowels)
print(consonents)