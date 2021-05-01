'''
Program :- Given a string as input. Remove digits from string.

Author :- AmRiyaz

LastModified :- April 2021
'''

st = "Won100"
len1 = len(st)
newSt = ""
for i in range(0,len1):
    ch = st[i]
    if((ch>="a" and ch<="z") or (ch>="A" and ch<="Z")):
        newSt = newSt + ch
print(newSt)

'''
Output:
Won
'''