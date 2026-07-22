list = [6,5,4,3,2,1]
print(list)
left = 0
right = len(list)-1
while left < right:
    list[left], list[right] = list[right], list[left]
    left+=1
    right-=1

print(list)