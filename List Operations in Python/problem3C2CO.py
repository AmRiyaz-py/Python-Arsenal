'''
Program :-Given a List as input. For each element in the given List if it is odd then 
           convert it to the next even number.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = [4,5,8,9,12]
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if(ch%2 !=0):
        ch = ch+1
    print(ch)

'''
Output:
4
6
8
10
12
'''