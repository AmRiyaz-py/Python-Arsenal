'''
Program:- Given a string as input. Print total number of uppercase and lowercase 
            characters. Note: String can contain non-alphabets.

Author:- AmRiyaz

Last Modified:- May 2021
'''
st = "AmmarRiyaz162z"
lenOfSt = len(st)
upSt = 0
lowSt = 0
for i in range(0,lenOfSt):
    ch = st[i]
    if(ch >= "A" and ch <= "Z"):
        upSt = upSt + 1
    if(ch >= "a" and ch<="z"):
        lowSt = lowSt + 1
print("Upper : ",upSt)
print("Lower : ",lowSt)

'''
Output:-
Upper :  2
Lower :  9
'''