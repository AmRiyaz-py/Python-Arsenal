'''
Program :-Given a list of string as input.
         Create a new list of strings which have length >  2.

Author :- AmRiyaz

Last Modified :- April 2021
'''
list = ["aa","bbb","c","dddd","e","ff"]
lenOfList = len(list)
newList =[]
for i in range(0,lenOfList):
    ch = list[i]
    lenOfEle = len(ch)
    if(lenOfEle > 2):
        newList.append(ch)
print(newList)

'''
Output:
['bbb', 'dddd']
'''