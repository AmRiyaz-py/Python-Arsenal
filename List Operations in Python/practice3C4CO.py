'''
Program :-Given a list of string as input. Each string in the list should be doubled. So 
            "abc" becomes "abcabc".

Author :- AmRiyaz

Last Modified :- April 2021
'''
list = ["abc","ammar"]
lenOfList = len(list)
newList = []
for i in range(0,lenOfList):
    ch = list[i]
    lenOfEle = len(ch)
    newList.append(ch+ch)
print(newList)

'''
Output:
['abcabc', 'ammarammar']
'''