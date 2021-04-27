'''
Program : Problem for practice

Author : AmRiyaz

Last Modified : April 2021
'''
m = 3
st =""
p ="x"
for i in range(1, m+1):
    st = st + p
p = p+"y"
n = m
for i in range(1, m+1):
    st = st+p+str(n)
    n = n-1
print(st)

'''
Output:-
xxxxy3xy2xy1
'''
