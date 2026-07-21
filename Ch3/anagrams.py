# s1 = "listen"
# s2 = "silent"
# print(s1, s2)
# s1 = "".join(sorted(s1))
# s2 = "".join(sorted(s2))
# if s1 == s2:
#     print("True")
# else:
#     print("False")

s1 = "listen"
s2 = "silent"
print(s1, s2)

if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")