'''
Program :-Given a string list and a string as input. It prints the count of input string in 
            input list

Author :- AmRiyaz

Last Modified :- April 2021
'''
list = ["1","3","1","1","3"]
lenOfList = len(list)
inputSt = "1"
count = 0 
for i in range(0,lenOfList):
    ch = list[i]
    if(ch == inputSt):
        count = count + 1
print(count)

'''
Output:
3
'''