# Exercise 1
import random

def all_the_snacks(snack):
    print(snack * 100)

snacks = ['Snickers', 'Marathon', 'Jelly Beans', 'Chocolate']
snack = snacks[random.randint(0, len(snacks) - 1)]
all_the_snacks(snack)
all_the_snacks(2)

# Exercise 2

def all_the_snacks(snack, spacer):
    print((snack + spacer) * 100)

all_the_snacks(snack, '--')
# all_the_snacks(2, '--')
# all_the_snacks(2, 4)


# Exercise 3

def all_the_snacks(snack, spacer, num):
    print((snack + spacer) * num)

all_the_snacks(snack, '--', 5)


# Exercise 4

def in_grocery_list(grocery_item):
    groceries = ['Cheese', 'Milk', 'Ham', 'Eggs']
    print(grocery_item in groceries)

in_grocery_list('Ham')
in_grocery_list('Chocolate')


# Exercise 5

def price_matcher():
    groceries = ['Cheese', 'Milk', 'Ham', 'Eggs']
    prices = [2.10, 1.50, 7.40, 10.30, 12.0]
    print(random.choice(groceries))
    print(random.choice(prices))

price_matcher()


# Exercise 6

def price_matcher():
    groceries = ['Cheese', 'Milk', 'Ham', 'Eggs']
    prices = [2.10, 1.50, 7.40, 10.30, 12.0]
    return random.choice(groceries), random.choice(prices)

def free_change():
    grocery, price = price_matcher()
    print(grocery + " £" + str(abs(price - 10.0)))

free_change()
