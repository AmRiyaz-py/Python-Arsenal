'''
Program :- Given n as input , print
           => print "Grade A" if the number is greater than and equal to 90
           => print "Grade B" if the number is greater than and equal to 80
           =>print "Grade C" if the number is greater than and equal to 60
           => print "Grade D" if the number is greater than and equal to 30

Author :- AmRiyaz

Last Modified :- April 2021
'''
n = 96
if(n >= 90):
    print("Grade A")
elif(n >= 80):
    print("Grade B")
elif(n >= 60):
    print("Grade C")
elif(n >= 30):
    print("Grade D")

'''
Output:
when n = 96 
=> Grade A
when n = 75
=> Grade C
when n = 33
=> Grade D
'''