'''Python comprehensions are a very natural and easy way
to create lists, dicts, and sets. They are also a great
alternative to using maps and filters within python. If
you are using maps, filters, or for loops to create your
lists, then most likely you could and should be using
comprehensions instead.
'''

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want 'n' for each 'n' in nums
# 1. Using for loop
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# 2. Using list comprehension
my_list = [n for n in nums]
print(my_list)

# I want 'n * n' for each 'n' in nums
# 1. Using for loop
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

# 2. Using map + lambda
my_list = map(lambda n: n * n, nums)
print(list(my_list))

# 3. Using list comprehension
my_list = [n * n for n in nums]
print(my_list)

# I want 'n' for each 'n' in nums if 'n' is even
# 1. Using for loop
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# 2. Using filter + lambda
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list)

# 3. Using list comprehension
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each num in '0123'
# 1. Using for loop
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# 2. Using list comprehension
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# I want a dict{'name': 'hero'} for each name hero in list(zip(names, heros))
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# 1. Using zip function
print(list(zip(names, heros)))

# 2. Using for loop
my_dict = {}
for name, hero in list(zip(names, heros)):
    my_dict[name] = hero
print(my_dict)

# 3. Using dictionary comprehension
my_dict = {name: hero for name, hero in list(zip(names, heros))}
print(my_dict)

# 4. More complicated
my_dict = {name: hero for name, hero in list(
    zip(names, heros)) if name != 'Peter'}
print(my_dict)

# Set comprehensions
nums = [1, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9]

# 1. Using for loop
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# 2. Using set comprehension
my_set = {n for n in nums}
print(my_set)
