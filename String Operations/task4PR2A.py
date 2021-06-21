'''
Program:- Given a string as input. Print capital if we encounter capital letter. Print small 
            otherwise. Assume string contains only alphabets

Author:- AmRiyaz

Last Modified:-
'''
st = "JerRy"
lenOfSt = len(st)
for i in range(0,lenOfSt):
    ch = st[i]
    if(ch >= "A" and ch <= "Z"):
        print(ch + " : capital" )
    if(ch >= "a" and ch <="z"):
        print(ch + " : lower")


'''
Output:-
J : capital
e : lower
r : lower
R : capital
y : lower
'''