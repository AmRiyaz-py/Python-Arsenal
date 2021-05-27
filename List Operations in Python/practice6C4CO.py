'''
Program :-Given a string list and a string as input. It prints "True" if
             this string is present 
             in list. It prints "False" if we cannot find this string in input list.

Author :- AmRiyaz

Last Modified :- April 2021
'''
list = ["Ammar","riyaz"]
lenOfList = len(list)
inputSt = "riyaz"
status = ""
for i in range(0,lenOfList):
    ch = list[i]
    if(ch == inputSt ):
        status = "True"
    else:
        status = "False"
print(status)

'''
Output:
True
'''