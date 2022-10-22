# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('id int_a is', id(int_a))
print('id str_b is', id(str_b))
print('id set_c is', id(set_c))
print('id lst_d is', id(lst_d))
print('id dict_e is', id(dict_e))


# 2. Append 4 and 5 to the lst_d and define the id one more time.
lst_d.extend([4, 5])
print('id lst_d is', id(lst_d))


# 3. Define the type of each object from step 1.
print('type of int_a is', type(int_a))
print('type of str_b is', type(str_b))
print('type of set_c is', type(set_c))
print('type of lst_d is', type(lst_d))
print('type of dict_e is', type(dict_e))


# 4*. Check the type of the objects by using isinstance.
print('type int_a is int', isinstance(int_a, int))
print('type str_b is str', isinstance(str_b, str))
print('type set_c is set', isinstance(set_c, set))
print('type lst_d is list', isinstance(lst_d, list))
print('type dict_e is dict', isinstance(dict_e, dict))


# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
#
# 5. With .format and curly braces {}
print('Anna has {} apples and {} peaches'.format(4, 5))

# 6. By passing index numbers into the curly braces.
print('Anna has {0} apples and {1} peaches'.format(4, 5))

# 7. By using keyword arguments into the curly braces.
print('Anna has {apple} apples and {peach} peaches'.format(apple =4, peach =5))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print('Anna has {apple:5} apples and {peach:3} peaches.'.format(apple =4, peach =5))

# 9. With f-strings and variables
apple =4
peach =5
print(f"Anna has {apple} apples and {peach} peaches.")

# 10. With % operator
print("Anna has %(apples)s apples and %(peaches)s peaches." % {"apples": apple, "peaches": peach})

# 11*. With variable substitutions by name (hint: by using dict)
mydict = {'apples': apple, 'peaches': peach}
print('Anna has {} apples and {} peaches'.format(mydict['apples'], mydict['peaches']))

#
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#(2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#
# 12. Convert (1) to list comprehension
lst = [num**2 if num % 2 == 1 else num**4 for num in range(10)]
print(lst)

# 13. Convert (2) to regular for with if-else
lst = []
for num in range(10):
    if num % 2 == 0:
        lst.append(num // 2)
    else:
        lst.append(num * 10)
print(lst)

# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
#
# 14. Convert (3) to dict comprehension.
mydict = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(mydict)

# 15*. Convert (4) to dict comprehension.
dict_comprehension = {num: num**2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comprehension)

# 16. Convert (5) to regular for with if.
mydict = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        mydict[num] = num ** 3
print(mydict)

# 17*. Convert (6) to regular for with if-else.
mydict = {}
for num in range(10):
    if num ** 3 % 4 == 0:
        mydict[num] = num ** 3
    else:
        mydict[num] = num
print(mydict)
#
# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
#
# 18. Convert (7) to lambda function
foo = lambda x, y: x if x < y else y

# 19*. Convert (8) to regular function
def foo(x, y, z):
    if y < x & x > z:
        return z
    else:
        return y

# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# 20. Sort lst_to_sort from min to max
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

# 21. Sort lst_to_sort from max to min
lst_to_sort.sort(reverse=True)
print(lst_to_sort)

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
mylist = list(map(lambda x: x*2, lst_to_sort))
print(mylist)

# 23*. Raise each list number to the corresponding number on another list:
# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
list_A = [2, 3, 4]
list_B = [5, 6, 7]
mylist= list(map(lambda x, y: x**y, list_A, list_B))
print(mylist)

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
mylist = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(mylist)

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
b = range(-10, 10)
mylist = list(filter(lambda numbers: numbers < 0, b))
print(mylist)

# 26*. Using the filter function, find the values that are common to the two lists:
# list_1 = [1,2,3,5,7,9]
# list_2 = [2,3,5,6,7,8]
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
mylist = list(filter(lambda common: common in list_2, list_1))
print(mylist)
