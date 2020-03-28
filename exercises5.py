# Exercise 1
import random

def all_the_snacks(snack, spacer=', ', num=10):
    print((snack + spacer) * num)

# Exercise 2
all_the_snacks('Snickers')
all_the_snacks('Snickers', '--')
all_the_snacks('Snickers', '--', 5)

all_the_snacks(spacer='--', num=8, snack='Snickers')
