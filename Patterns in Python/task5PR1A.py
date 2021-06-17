'''
Program:-Given n as input. Print following pattern using For loop.
#
#
#
#
#
5
4
3
2
1

Author:- AmRiyaz

Last Modified:- May 2021
'''
n = 5
hash = "#"
a = ""
for i in range(1,n+1):
    a = hash
    print(a)
for i in range(1,n+1):
    print(n)
    n = n-1

'''
Output:
#
#
#
#
#
5
4
3
2
1
'''