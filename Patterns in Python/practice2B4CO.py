'''
Program :-Given a string as input. Create a new string according to following pattern

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = "cat"
newSt = ""
lenOfst = len(st)
for i in range(0,lenOfst):
    ch = st[i]
    newSt = newSt + ch
    print(ch)
    
'''
Output:
c
a
t
'''
