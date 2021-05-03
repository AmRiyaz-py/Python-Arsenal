
'''
Program :-Given a List as input. Print all even numbers

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = [10,9,12,14,23]
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if(ch%2 == 0):
        print(ch)

'''
Output:-
10
12
14
'''