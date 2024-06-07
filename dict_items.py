# dict.items() makes keys and values accessible independently of one another:
#EXAMPLE_1:

my_dict = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
x = my_dict.items()
print(x)
# Output will be: dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# It will be printed as tuples within a list.