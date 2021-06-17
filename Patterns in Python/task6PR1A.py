'''
Program:- Given n as input. Print following pattern using For loop.
5
54
543
5432
54321

Author:- AmRiyaz

Last Modified:- May 2021
'''
n = 5
a = ""
for i in range(1,n+1):
    a = a + str(n) 
    print(a)
    n = n - 1
    
'''
Output:
5
54
543
5432
54321
'''