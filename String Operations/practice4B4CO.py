'''
Program :-Given a string as input. Create a new string containing characters that are 
            present at even numbered position in input string. 
            Note: We’ll add character at 0th position also.

Author :- AmRiyaz

Last Modified :- April 2021
'''
st = "amcar"
lenOfst = len(st)
newSt = ""
for i in range(0,lenOfst):
    if(i%2==0):
        ch = st[i]
        newSt = newSt + ch
print(newSt)

'''
Output:
acr
'''