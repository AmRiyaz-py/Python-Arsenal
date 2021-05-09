'''
Program :-Given a list of string as input. Print total number of chars in the list.

Author :- AmRiyaz

Last Modified :- April 2021
'''
list = ["aba","ab","d"]
lenOfList = len(list)
count = 0
TotalLength = 0
for i in range(0,lenOfList):
    ch = list[i]
    lenOfEle = len(ch)
    TotalLength = TotalLength + lenOfEle
print(TotalLength)

'''
Output:
6
'''