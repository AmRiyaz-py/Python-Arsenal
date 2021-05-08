'''
Program :-Given a string as input. Create a new string containing double the characters 
             from input string.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = "world"
newSt = ""
lenOfst = len(st)
for i in range(0,lenOfst):
    ch = st[i]
    newSt = newSt+ch
    newSt = newSt+ch
print(newSt)

'''
Output:
wwoorrlldd
'''