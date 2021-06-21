'''
Program:- Given a string as input. Give count of character 'x' and 'y' in given string

Author:- AmRiyaz

Last Modified:- May 2021
'''
st = "exactly"
lenOfSt = len(st)
xSt = 0
ySt = 0
for i in range(0,lenOfSt):
    ch = st[i]
    if(ch == "x"):
        xSt = xSt + 1
    if(ch == "y"):
        ySt = ySt + 1
print("x#",xSt)
print("y#",ySt)

'''
Output:-
x# 1
y# 1
'''