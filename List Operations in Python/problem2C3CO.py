'''
Program :-Given a List of size n as input. Create a new List, where first element of
            original List is not there. Assume List of minimum 1 length.

Author :- AmRiyaz

Last Modified :- April 2021
'''
oldList = [12,10,3,4,5]
newList = []
lenOfOL = len(oldList)
for i in range(1,lenOfOL):
    ch = oldList[i]
    newList.append(ch)
print(newList)

'''
Output:
[10, 3, 4, 5]
'''