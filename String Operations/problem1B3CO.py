'''
Program :- Given a string as input. Remove all a's from the string

Author :- AmRiyaz

LastModified :- April 2021
'''

st = "global"
len1 = len(st)
newSt = ""
for i in range(0,len1):
    ch = st[i]
    if(ch != "a"):
        newSt = newSt+ch
print(newSt)

'''
Output:
globl
'''