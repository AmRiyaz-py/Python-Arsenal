'''
Program :-Given a List of size n as input. Create a new List with double the size of 
            original where the elements of first List are repeated one more time.

Author :- AmRiyaz

Last Modified :- April 2021
'''
oldList = [4,1,7,9]
lenOfOL = len(oldList)
newList = []
for i in range(0,lenOfOL):
    ch = oldList[i]
    newList.append(ch)
for i in range(0,lenOfOL):
    ch = oldList[i]
    newList.append(ch)
print(newList)

'''
Output:
[4, 1, 7, 9, 4, 1, 7, 9]
'''