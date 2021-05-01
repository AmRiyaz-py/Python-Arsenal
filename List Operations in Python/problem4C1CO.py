'''
Program :-Given a list as input. Print sum of even and sum of odd elements.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = [12,1,5,8,4,7]
sumEven  = 0
sumOdd = 0
len1 = len(st)
for i in range(0,len1):
    ch = st[i]
    if(ch%2 == 0):
        sumEven = sumEven + ch
    else:
        sumOdd = sumOdd + ch
print("Sum Even : ",sumEven)
print("Sum Odd : ",sumOdd) 

'''
Output:
Sum Even :  24
Sum Odd :  13
'''