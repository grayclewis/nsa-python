# Exercise 1 & 7

shopping_list = {'Tea': 9.42, 'Bread': 5.67, 'Milk': 3.25, 'Cerial': 13.40, 'Beer': 7.50}
print(shopping_list.keys())

for key, value in shopping_list.items():
    print(key)


# Exercise 2

total = 0.0
for key, value in shopping_list.items():
  total += total + value

print(total)

# Exercise 3

shopping_list = {'Tea': 9.42, 'Bread': 5.67, 'Milk': 3.25, 'Cerial': 13.40, 'Beer': (7.50 * 5)}
total = 0.0
for k, v in shopping_list.items():
  total += total + v

print(total)


# Exercise 4
print(len("blood-oxygenation level dependent functional magnetic resonance imaging"))

# Exercise 5
print("Fruit " * 100)

# Exercise 6
# dir("Hello")
# help("Hello".join)
print('ABC'.join(['1', '2', '3']))
