principal = 436800
payment = 1595.42
rate = 0.0192
total_paid = 0

# Extra payment info
extra_payment = 0
extra_payment_start_month = 1
extra_payment_end_month = 60
month = 0

out =  open('schedule.txt', 'w') # Open a file for writing
print('{:>5s} {:>10s} {:>10s} {:>10s}'.format('Month', 'Interest', 'Principal', 'Remaining'), file=out)
while principal > 0 :
    month +=1
    if month >=extra_payment_start_month and month <=extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    interest = principal*(rate/12)
    principal = principal + interest - total_payment
    total_paid += total_payment
    print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'.format(month, interest, total_payment - interest, principal), file=out)

out.close()
print('Total paid:', total_paid)