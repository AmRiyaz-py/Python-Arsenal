'''
Program :-Given a list as input. Print number of elements greater than 10.

Author :- AmRiyaz

Last Modified :- April 2021
'''

st = [1,10,12,5,22]
count = 0
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if (ch>10):
        count= count+1
print(count)
'''
Output:
2
'''