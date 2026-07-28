# Given a list of numbers, use a dictionary to find the first number that appears more than once.

mylist = [1,3,4,5,6,6,7,7,7]
print(mylist)
mydist = {}

for num in mylist:
    if num in mydist:
        print('the first repeated no', num)
        break
    else:
        mydist[i]=1
else:
    print('no repeated no')