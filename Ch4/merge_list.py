num1 = [1,3,5,9]
num2 = [2,4,6,8]

result = []

i = 0
j = 0

while i < len(num1) and j < len(num2):
    if num1[i]<num2[j]:
        result.append(num1[i])
        i+=1
    else:
        result.append(num2[j])
        j+=1
while i < len(num1):
    result.append(num1[i])
    i+=1

while j < len(num2):
    result.append(num2[j])
    j+=1

print(result)