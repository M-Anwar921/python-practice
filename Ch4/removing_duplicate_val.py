num = [1,2,2,3,3,3,4,5,6,7,7]
print(num)

seen = set()
result = []

for i in num:
    if i not in seen:
        seen.add(i)
        result.append(i)

print(result)