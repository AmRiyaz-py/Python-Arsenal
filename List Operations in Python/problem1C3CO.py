'''
Program :-Given a list as input. Create a new list in which each element is 3 times the 
            original.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = [1,3,4,7]
newSt = []
len1 = len(st)
for i in range(0, len1):
    ch = st[i]
    thrice = 3 * ch
    newSt.append(thrice)
print(newSt)
    
'''
Output:
[3, 9, 12, 21]
'''