'''
Program :- Program for understanding of elif

Author :- AmRiyaz

Last Modified :- April 2021
'''
n = 5
m = 3
st = ""
ptr = "X"
for i in range(1,n+1):
    if(i % 3 == 1):
        st = st + ptr
    elif(i % 3 ==2):
        st  = st + "Y"
    else:
        st  = st + "Z"
print(st)


'''
Output:
XYZXY
'''