'''
Program :-String program example in python.

Author :- AmRiyaz

Last Modified :- April 2021
'''
name = "1D0I#L0L#I"
hash = "#"
strA = ""
strN = ""
strH = ""
len1=len(name)
for i in range(0,len1):
    zch = name[i]
    if (zch == hash):
        strH = strH + zch
    if(zch >= "A" and zch <="z"):
        strA = strA + zch
    if(zch >= "0" and zch <="9"):
        strN = strN + zch
strA = strA + strH + strN
print(strA)

'''
Output:
DILLI##100
'''