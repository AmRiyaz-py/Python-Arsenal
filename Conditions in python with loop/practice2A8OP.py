'''
Program : Problem for practice

Author : AmRiyaz

Last Modified : April 2021
'''
n = 5
m = 1
st = ""
for i in range(1,n+1):
    st = st+str(m)
    m = m+1
m = m-2
for i in range(1, n+1):
    st = st + str(m)
    m = m-1
print(st)

'''
Output:-
1234543210
'''