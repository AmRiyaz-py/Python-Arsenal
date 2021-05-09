'''
Program :-Given a list of string as input. Print number of strings with length > 2.

Author :- AmRiyaz

Last Modified :- April 2021
'''
list = ["aa","bbb","c","dddd","e","ff"]
lenOfList = len(list)
count = 0
for i in range(0,lenOfList):
    ch = list[i]
    lenOfEle = len(ch)
    if(lenOfEle > 2):
        count = count+1
print(count)

'''
Output:
2
'''