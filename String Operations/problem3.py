'''
Program :- Given a string as input. Print 'number:found'if we encounter '1', '2' or '3' in 
             the string.

Author :- AmRiyaz

Last Modified :- April 2021
'''

st = "one2three342"
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if(ch == str(1) or ch == str(2) or ch == str(3)):
        print(ch+":"+"found")

'''
Output:
2:found
3:found
2:found
'''