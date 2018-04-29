# Python code to demonstrate copy operations

# importing "copy" for copy operations
import copy

# initializing list 1
list1 = [1, 2, [3, 5], 4]

# using deepcopy to deep copy
list2 = copy.deepcopy(list1)


# original elements of list
print("The original elements before deep copying")
for i in range(0, len(list1)):
    print(list1[i], type(list1[i]), end=" ")

print("\r")

# adding and element to new list
list2[2][0] = 7

# Change is reflected in l2
print("The new list of elements after deep copying ")
for i in range(0, len(list1)):
    print(list2[i], end=" ")

print("\r")

# Change is NOT reflected in original list
# as it is a deep copy
print("The original elements after deep copying")
for i in range(0, len(list1)):
    print(list1[i], end=" ")
print('\r')

# Shallow copy is directly referencing list1 to list2.
list2 = list1
# if any changes made to list2 will affect changes in list1. But that has not appeared in deep copy
list2[2][0] = 7
# now list1 value has changes even though we have made change on list2
print(list1)
