# Tuple with 5 elements
my_tuple = ("goga", "giorgi", "luka", "nika", "sandro")

# Unpacking the tuple
name1, name2, name3, *rest = my_tuple

print(name1,)
print(name2)
print(name3)
print(rest)