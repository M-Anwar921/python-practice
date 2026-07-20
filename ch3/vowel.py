s=input("Enter a string: ")
count = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']
for char in s:
    if char in vowels:
        count=count+1
print(count)
