'''
Program :- Given n as input, 
            => Print "C" if the number is divisible by 3
            => Print "B" if the number (on divison with 3) leaves remainder 2
            => Print "A" if the number (on divison with 3) leaves remainder 1
           
Author :- AmRiyaz

Last Modified :- April 2021
'''
n = 5
a = ""
for i in range(1,n+1):
    if(i % 3 == 0):
        a = a + "C"
    if(i % 3 == 2):
        a = a + "B"
    if(i % 3 == 1):
        a = a + "A"
print(a)

'''
Output : 
ABCAB
'''