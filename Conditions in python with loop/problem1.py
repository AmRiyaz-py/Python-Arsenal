
'''
Program : Given n as input , print the following pattern
when n = 3,
=>
1
2
3
2
1

Author : AmRiyaz

Last Modified : April 2021
'''
n = 3
a = 1
for i in range(1,n+1):
    print(a)
    a=a+1
a= a-2
for i in range(1,n):
    print(a)
    a= a-1

'''
Output :-
1
2
3
2
1
0
'''