def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
    return size_to_ounce_map[size]

print(pour_coffee("tall"))
print(pour_coffee("grande"))
print(pour_coffee("jumbo"))
print(pour_coffee("venti"))

# Getting Data
#To add a value to "jumbo" we use dict.get method like so:
def pour_coffee(size):
    size_to_ounce_map = {
        "tall": 12,
        "grande": 16,
        "venti": 20,
    }
    return size_to_ounce_map.get(size, "Please Enter a valid cup size")
# I have changed the return value
# dict.get method takes two values: key and value.
# In this case: key is size, value is "Please Enter a valid cup size".

print(pour_coffee("tall"))
print(pour_coffee("grande"))
print(pour_coffee("jumbo"))
print(pour_coffee("venti"))