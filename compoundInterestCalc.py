#Compund Interest = Principal(1 + rate/100)**total time
import math
principal=0
rate=0
time=-1

while(True):
    if(principal<=0):
        principal=int(input("Enter the Principal Amount --> "))
    else:
        break

while(True):
    if(rate<=0):
        rate=float(input("Enter the Rate of interest --> "))
    else:
        break

while(True):
    if(time<0):
        time=int(input("Enter the Time period for which money is to be invested in years --> "))
    else:
        break


total=principal * pow(1+rate/100,time)
print(f"Total Amount --> {total:.2f} Interest Amount --> {total - principal:.2f}")