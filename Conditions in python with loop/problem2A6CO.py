'''
Program :- Given n as input , for every number from 1 to n:
           => print D if the number is divisble by 4
           => print C if the number (on division with 4) leaves remainder 3
           => print B if the number (on division with 4) leaves remainder 2
           => print A if the number (on division with 4) leaves remainder 1

Author :- AmRiyaz

Last Modified :- April 2021
'''
n = 5
st = ""
for i in range(1,n+1):
    if( i % 4 == 0):
        st = st + "D"
    elif( i % 4 == 3):
        st = st + "C"
    elif( i % 4 == 2):
        st = st + "B"
    elif( i % 4 == 1):
        st = st + "A"
print(st)
    



'''
Output:
ABCDA
'''