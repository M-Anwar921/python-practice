num = [1,1,3,3,5,5,5,7,8,9]

count = {}

for i in num:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1

for i in count:
    print(i, "appears" , count[i], "times")
