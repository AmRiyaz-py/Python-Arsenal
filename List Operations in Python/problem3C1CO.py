'''
Program :-Given a list as input. Print sum of even elements.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = [1,2,12,5]
sumOfEven = 0
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if(ch%2==0):
        sumOfEven = sumOfEven + ch
print(sumOfEven)

'''
Output:
14
'''