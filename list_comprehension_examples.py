# lets make an exercise for list comprehension
# you have a code block like this

# a=[]
# for i in range(1, 11):
#     if i % 2 == 0:
#         a.append(i)
# print(a)
# # [2, 4, 6, 8, 10] result
#
# a=[]
# for i in range(1, 11):
#     if i % 2 == 0:
#         a.append(i**2)
# print(a)
# # [4, 16, 36, 64, 100]


# first i is output
# second i is variable
# if block is filter condition

a=[i for i in range(1, 11) if i % 2 == 0]
print(a)
# [2, 4, 6, 8, 10] result

a=[i**2 for i in range(1, 11) if i % 2 == 0]
print(a)
# [4, 16, 36, 64, 100] result