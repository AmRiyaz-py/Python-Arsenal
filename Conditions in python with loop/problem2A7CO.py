'''
Program : Given n as input, print following pattern:
            n#....5#4#...(starting from n reverse to 1)

Author : AmRiyaz

Last Modified : April 2021
'''
n = 5
num = n
st = ""
for i in range(1, n+1):
    st = st + str(num) + "#"
    num = num-1
print(st)

'''
Output:
5#4#3#2#1#
'''