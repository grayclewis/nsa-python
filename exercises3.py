# Exercise 1

items = [9.42, 5.67, 3.25, 13.40, 7.50]
print(min(items))
print(max(items))

# Exercise 2

import random
# help(random.randint)
snack = 'Toffee'
print(snack * random.randint(0, 100))


# Exercise 3

print(dir(random))

print(items[random.randint(0, len(items) - 1)])
print(random.choice(items))


# Exercise 4

print(round(items[random.randint(0, len(items) - 1)]))


# Exercise 5
item = items[random.randint(0, len(items) - 1)]
diff = item - 10.0
print(abs(diff))

# if item < 10.0:
#     print(10.0 - item)
# else:
#     print(item - abs(item - 10.0))
