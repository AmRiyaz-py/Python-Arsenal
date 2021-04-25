'''
Program : Example related to string operation

Author : AmRiyaz

Last Modified : April 2021
'''

n = 5
px = ""
py="Y"
z = n*2
for i in range(1,n+1):
    px = px+py+str(z)
    print(px)
    z= z-2

'''
Output : 
Y10
Y10Y8    
Y10Y8Y6  
Y10Y8Y6Y4
Y10Y8Y6Y4Y2
'''