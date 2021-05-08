'''
Program :-Given a string as input. Reverse it.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = "ammar"
lenOfst = len(st)
revSt  = ""
for i in range(0,lenOfst):
    ch = st[i]
    revSt = ch + revSt
print(revSt)

'''
Output:
ramma
'''