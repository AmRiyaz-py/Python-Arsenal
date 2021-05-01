'''
Program :- Given a string as input. Create a new string containing only lowercase 
            characters.

Author :- AmRiyaz

LastModified :- April 2021
'''

st ="AmmArBAbg"
newSt = ""
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if(ch>="a" and ch<="z"):
        newSt = newSt + ch
print(newSt)

'''
Output:
mmrbg
'''