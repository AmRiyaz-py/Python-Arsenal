'''
Program:- Given a string as input. Check and print how many times character 'z' is 
            present in the given string?

Author:- AmRiyaz

Last Modified:- May 2021
'''
st = "Amzzmarz"
lenOfSt = len(st)
total = 0
for i in range(0,lenOfSt):
    ch = st[i]
    if(ch=="z"):
        total = total + 1
print(total)

'''
Output:-
3
'''