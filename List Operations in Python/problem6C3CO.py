'''
Program :-Given a List as input. Print difference of largest and smallest element in List.

Author :- AmRiyaz

Last Modified :- April 2021
'''
list  = [5,2,3,1,7,8]
len1 = len(list)

min= list[0]
max = list[0]
for i in range(0,len1):
    ch = list[i]
    
    if (ch < min):
        min = ch
    if(ch > max):
        max = ch
diff = max - min        
print(diff)


'''
Output:
7
'''