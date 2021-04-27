'''
Program : Given n as in input , print the following pattern.
when n = 10 => 10$11$12$13$14$15$14$13$12$11$10$

Author : AmRiyaz

Last Modified : April 2021
'''

st = ""
a ="$"
n = 10
b = 6
for i in range(1,b+1):
    st = st + str(n) + a
    n = n + 1
n = n-2
for i in range(1,b):
    st = st + str(n) + a
    n = n - 1
print(st)

'''
Output:-
10$11$12$13$14$15$14$13$12$11$10$9$
'''