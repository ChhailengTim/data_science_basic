year = 0
tuition = 10000

while tuition < 20000:
    year += 1
    tuition += tuition * 0.07
print("The number of years it will take for the tuition to x2 is: ", year)