'''
Program :-Given a List as input. Print the smallest element in List

Author :- AmRiyaz

Last Modified :- April 2021
'''

st = [10,2,12,15]
len1 = len(st)
min = st[0]
for i in range(0,len1):
    ch = st[i]
    if(ch<min):
        min = ch
print("The smallest element is:-",min)

'''
Output:
The smallest element is:- 2
'''