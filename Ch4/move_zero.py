num = [1,0,4,0,8,9]
print(num)

result = []


i = 0
j=1
count = 0
while i < len(num):
    if num[i] == 0:
        count+=1 
        i+=1
    elif num[i] != 0:
        result.append(num[i])
        i+=1

while j <= count:
    result.append(0)
    j+=1

print(result)