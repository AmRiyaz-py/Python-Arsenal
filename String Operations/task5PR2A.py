'''
Program:- Count digits and alphabets in input string. Assume string contains only 
        alphabets and digits.
        Note: Input string can contain letters in both the cases. 

Author:- AmRiyaz

Last Modified:- May 2021
'''
st = "Jerry27"
lenOfSt = len(st)
alpha = 0 
digi = 0
for i in range(0,lenOfSt):
    ch = st[i]
    if((ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z")):
        alpha = alpha + 1
    if(ch >= "0" and ch <="9"):
        digi = digi + 1
print("Digit : ",digi)
print("Alphabet : ",alpha)

'''
Output:-
Digit :  2
Alphabet :  5
'''