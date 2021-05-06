'''
Program :-Given a List of size n as input. Create a new List, where first element is 0, and 
             rest elements are same as original List

Author :- AmRiyaz

Last Modified :- April 2021
'''
oldList = [5,2,1,7]
lenOfOL = len(oldList)
newList = [0]

for i in range(0,lenOfOL):
    ch = oldList[i]
    newList.append(ch)
print(newList)

'''
Output:
[0, 5, 2, 1, 7]
'''