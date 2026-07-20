array = [1, -8,4,7,9,4,3,8]
print(array)
min_val = array[0]
max_val = array[0]
for val in array:
    if max_val < val:
        max_val = val
    if min_val > val:
        min_val = val


print("The min value is: ", min_val)

print("The max value is: ", max_val)