'''
Program :-Given a string as input containing digits, uppercase and lowercase characters. 
            Create a new string that shifts all digits in front, lowercase in middle and 
            uppercase at the end.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = "2JerrY7"
lenOfst = len(st)
upSt = ""
lowSt = ""
numSt = ""
newSt = ""
for i in range(0,lenOfst):
    ch = st[i]
    if(ch>="A" and ch<="Z"):
        upSt = upSt + ch
    if(ch>="a" and ch<="z"):
        lowSt = lowSt + ch
    if(ch>="0" and ch<="9"):
        numSt = numSt + ch
newSt = numSt + lowSt + upSt
print(newSt)

'''
Output:
27errJY
'''