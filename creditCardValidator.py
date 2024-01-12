# Test Credit Card Account Numbers
# American Express 378282246310005
# American Express 371449635398431
# American Express Corporate 378734493671000
# Australian Bankcard 5610591081018250
# Diners Club 30569309025904
# Diners Club 38520000023237
# Discover 6011111111111117
# Discover 6011000990139424
# JCB 3530111333300000
# JCB 3566002020360505
# MasterCard 5555555555554444
# MasterCard 5105105105105100
# Visa 4111111111111111
# Visa 4012888888881881

# Python credit card validator program

# 1. Remove any '-' or ' '
# 2. Add all digits in the odd places from right to left
# 3. Double every second digit from right to left.
#        (If result is a two-digit number,
#        add the two-digit number together to get a single digit.)
# 4. Sum the totals of steps 2 & 3
# 5. If sum is divisible by 10, the credit card # is valid

odd_sum=0
even_sum=0
totals=0

cardNumber = input("Enter Your Card number --> ")
cardNumber = cardNumber.replace("-","")
cardNumber=cardNumber.replace(" ","")

for i in cardNumber[-1::-2]:
    i=int(i)
    odd_sum+=i

for i in cardNumber[-2::-2]:
    i=int(i)
    i*=2
    if (len(str(i))==2):
        i=str(i)
        temp1=int(i[0])
        temp2=int(i[1])
        even_sum=temp1+temp2

totals=odd_sum+even_sum
print(f"{odd_sum} {even_sum} {totals}")

if(totals%10==0):
    print(f"{cardNumber} is Valid!")
else:
    print(f"{cardNumber} is Invalid!")