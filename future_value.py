future_value = float(input('Enter the desired future value: '))
rate = float(input('Enter the annual interest rate: '))
years = int(input('Enter the number of years the money will grow: '))

present_value = future_value / (1 + rate) ** years

print('You wil need to deposit this amount:', present_value)
