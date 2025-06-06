days = eval(input('Enter number of days: '))

years = days // 365
remaining_days = days % 365 

months = remaining_days // 30
days = remaining_days % 30

print('years =', years, '\nmonths =', months, '\ndays =', days)
