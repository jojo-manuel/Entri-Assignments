# Topic: List

# 1. Create a list of 5 random numbers and print the list
numbers = [10, 25, 5, 40, 15]
print("Original list:",numbers)


# 2. Insert 3 new values into the list
numbers.append(30)
numbers.append(50)
numbers.append(20)

print("Updated list:",numbers)


# 3. Print each element using a for loop
print("Each element in the list:")

for number in numbers:
    print(number)


# Topic: Dictionary

# 1. Create a dictionary
person = {
    "name": "John",
    "age": 25,
    "address": "New York"
}

print("Dictionary:", person)


# 2. Add phone number to the dictionary
person["phone"] = "1234567890"

print("Updated dictionary:", person)



# Topic: Set

# 1. Create a set
my_set = {1, 2, 3, 4, 5}

print("Original set:", my_set)


# 2. Add 6 to the set
my_set.add(6)

print("Set after adding 6:", my_set)


# 3. Remove 3 from the set
my_set.remove(3)

print("Set after removing 3:", my_set)


# Topic: Tuple

# 1. Create a tuple
my_tuple = (1, 2, 3, 4)

print("Tuple:", my_tuple)


# 2. Print the length of the tuple
print("Length of tuple:", len(my_tuple))