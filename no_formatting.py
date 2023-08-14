# This program demonstrates how a floating-point
# number is displayed with no formatting
# and number with formatting.
amount_due = 5000
monthly_payment = amount_due / 12.0
print('The monthly payment is', monthly_payment)
print('The monthly payment is', format(monthly_payment, '.2f'))
