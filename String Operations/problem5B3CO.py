'''
Program :- Given a string as input. Create a new string containing characters from input 
             with characters '0' and '5' replaced with character '#'.

Author :- AmRiyaz

LastModified :- April 2021
'''

st ="012345"
newSt = ""
a = "#"
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if(ch == "0" or ch == "5"):
        newSt = newSt + a
    else:
        newSt = newSt+ch
print(newSt)

'''
Output:
#1234#
'''