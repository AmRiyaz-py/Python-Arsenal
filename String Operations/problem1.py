'''
Program :- Given a string as input. Count number of a's in the string

Author :- AmRiyaz

Last Modified :- April 2021
'''

st = "abacd"
len1= len(st)
count = 0
for i in range(0,len1):
    ch = st[i]
    if(ch=="a"):
        count=count+1
print(count)

'''
Output:
2
'''