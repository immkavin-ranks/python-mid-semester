BASE_HOURS = 40
OT_MULTIPLIER = 1.5

def main():
	hours_worked = float(input('Enter the numbers '\
		+ 'of hours worked: '))
	pay_rate = float(input('Enter the hourly pay rate: '))

	if hours_worked > BASE_HOURS:
		calc_pay_with_OT(hours_worked, pay_rate)
	else:
		calc_regular_pay(hours_worked, pay_rate)


def calc_pay_with_OT(hours, rate):
	overtime_hours = hours - 40
	overtime_pay = overtime_hours * rate * OT_MULTIPLIER
	grosspay = BASE_HOURS * rate + overtime_pay
	print('The gross pay is $', \
		format(grosspay, ',.2f'), sep='')


def calc_regular_pay(hours, rate):
	grosspay = hours * rate
	print('the gross pay is $', \
		format(grosspay, ',.2f'), sep='')


main()