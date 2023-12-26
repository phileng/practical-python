# mortgage.py
#
# Exercise 1.7
# Exercise 1.8 add $1000 to payment for 1st year
# Exercise 1.9 add $1000 to payment between x and y months
#   answer is 310 payments and 880,074.10 total
#   answer is  payments and total same as above
# Exercise 1.10 add $1000 to payment between x and y months
#   make a table
# 1.11 fix overpayment at the end

startingprincipal = 500000.0
principal = startingprincipal
rate = 0.05
payment = 0
defaultpayment = 2684.11
total_paid = 0.0
payment_number = 1
extra_payment = 1000
extra_payment_start_month = (30 * 12) + 1
extra_payment_end_month = extra_payment_start_month + (30 * 12) - 1
ballonpayment = 2684.11 + extra_payment

while principal >= 0:
    payment = defaultpayment 
    
# last payment
#    if ( defaultpayment > principal):
#        payment = principal
# exit loop and update last total_paid 
    
#ballon payment
    if (payment_number >= extra_payment_start_month and payment_number <= extra_payment_end_month):
        payment = ballonpayment
#    print("Payment:", payment_number, "\t", payment)
#    print("Principal:", "\t", round(principal,2))
#    print("Paid:", round(total_paid,2))
    payment_number = payment_number + 1
    principal = principal * (1 + rate/12) - payment
    total_paid = total_paid + payment
#print("Total paid:", round(total_paid, 2))

printsummary = f'This ${startingprincipal} mortgage will need {payment_number} payments for a total of ${round(total_paid,2)} with a default payment of ${defaultpayment}.' 
print(printsummary)

