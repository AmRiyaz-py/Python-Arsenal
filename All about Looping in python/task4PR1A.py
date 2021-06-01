'''
Program:-Given n as input. Starting from 1 till n print 'Pepsi' if the number is divisible by 3 
            in following format. Print 'Coke' otherwise.

Author:- AmRiyaz

Last Modified:- May 2021
'''
n = 5
for i in range(1,n+1):
    if(i%3==0):
        print("Pepsi" +" - "+str(i))
    else:
        print("Coke"+" - "+str(i))


'''
Output:
Coke - 1
Coke - 2
Pepsi - 3
Coke - 4
Coke - 5
'''