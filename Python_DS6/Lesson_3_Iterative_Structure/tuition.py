

year = 0
tuition = 10000

while tuition < 20000:
    year = year + 1
    tuition = tuition + (tuition* 0.07)
    print('year:', year, ', tuition:', tuition)

print('It will take', year, 'years for the tuition to double.')