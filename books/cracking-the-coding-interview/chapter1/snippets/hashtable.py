# Creating a hashtable
my_dict = {}

# Adding key-value pairs to the hashtable
my_dict['apple'] = 3
my_dict['banana'] = 6
my_dict['orange'] = 4

# Accessing values from the hashtable
print(my_dict['apple'])  # Output: 3
print(my_dict['banana'])  # Output: 6

# Updating values in the hashtable
my_dict['apple'] = 5
print(my_dict['apple'])  # Output: 5

# Checking if a key exists in the hashtable
if 'banana' in my_dict:
    print("Banana is in the dictionary.")  # Output: Banana is in the dictionary.

# Removing a key-value pair from the hashtable
del my_dict['orange']
print(my_dict)  # Output: {'apple': 5, 'banana': 6}
