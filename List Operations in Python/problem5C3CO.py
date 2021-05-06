'''
Program :-Given a List of size n as input. Create a new List with double the size of 
            original where each element is duplicated.

Author :- AmRiyaz

Last Modified :- April 2021
'''
oldList = [1,2,3]
lenOfOL = len(oldList)
newList = []
for i in range(0,lenOfOL):
    ch = oldList[i]
    newList.append(ch)
    newList.append(ch)
print(newList)

'''
Output:
[1, 1, 2, 2, 3, 3]
'''