'''
Program:- Given n as input. Print sum of 4th power of all numbers from 1 to n. Check your 
            output against following set of inputs.

Author:- AmRiyaz

Last Modified:- May 2021
'''
n = 4
a = 0
res = 0 
for i in range(1,n+1):
    a = i*i*i*i
    res = res + a
print(res)

'''
Output:
354
'''