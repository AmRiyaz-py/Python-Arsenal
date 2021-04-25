'''
Program :- Given n as input, print table of n in following format

Author : AmRiyaz

Last Modified : April 2021
'''


n = 9
table = n
st = ""
for i in range(1,11):
    table = n*i
    st = str(n)+" X "+str(i)+" = "+str(table)
    print(st)

'''
Output:-
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50
'''