'''
Program :- Given a string as input. Count uppercase characters in the string.

Author :- AmRiyaz

LastModified :- April 2021
'''

st = "aaMmAr"
len1 = len(st)
count = 0
for i in range(0,len1):
    ch = st[i]
    if(ch>="A" and ch<="Z"):
        count = count+1
print(count)

'''
Output:
2
'''