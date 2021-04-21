'''
Program :- Given n as input, for every number form 1 to n ,
            print whether the number is even or odd

Author :- AmRiyaz

Last Modified :- April 2021
'''
n = 7
for i in range(1, n+1):
    if(i % 2 == 0):
        print(str(i)+" : "+"even")
    else:
        print(str(i)+ " : "+ "odd")