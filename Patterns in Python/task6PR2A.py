'''
Program:- Given a string as input. Print patterns according to following set of test cases.
j
j#
j#r
j#r#
j#r#y

Author:- AmRiyaz

Last Modified:- May 2021
'''
st = "jerry"
lenOfSt = len(st)
hash = "#"
newSt = ""
for i in range(0,lenOfSt):
    ch = st[i]
    if(i%2 == 1):
        ch = hash
    newSt = newSt + ch
    print(newSt)


'''
Output:-
j
j#
j#r
j#r#
j#r#y
'''