'''
Program :-Given a string as input containing uppercase and lowercase characters. 
        Create a new string that shifts all uppercase chars in front and lowercase at back

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = "AmMaR"
lenOfst = len(st)
upSt = ""
lowSt = ""
newSt = ""
for i in range(0,lenOfst):
    ch = st[i]
    if(ch>="A" and ch<="Z"):
        upSt = upSt + ch
    if(ch>="a" and ch<="z"):
        lowSt = lowSt + ch
newSt = upSt + lowSt
print(newSt)

'''
Output:
AMRma
'''