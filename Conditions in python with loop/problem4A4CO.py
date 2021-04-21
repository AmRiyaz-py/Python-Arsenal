'''
Program :- Given n as input, 
            => print "X" if the number is odd
            => print "Y" otherwise

Author :- AmRiyaz

Last Modified :- April 2021
'''
n = 5
a = ""
for i in range(1,n+1):
    if( i % 2 == 0):
        a = a + "Y"
    else:
        a = a + "X"
print(a)