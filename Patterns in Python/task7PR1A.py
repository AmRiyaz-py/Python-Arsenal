'''
Program:- Given n as input. Print following pattern using For loop.
1
12
123
1234
4
43
432
4321

Author:- AmRiyaz

Last Modified:- May 2021
'''
n = 4
a = 1
b = ""
c = ""
for i in range(1,n+1):
    b = b + str(a)
    print(b)
    a = a + 1
for i in range(1,n+1):
    c = c + str(n)
    print(c)
    n = n -1

'''
Output:
1
12
123
1234
4
43
432
4321
'''