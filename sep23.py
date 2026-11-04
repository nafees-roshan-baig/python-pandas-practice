# for i in range(4):#0123
#     if i == 2:
#         continue
#     for j in range(3):#012
#         if j == 2:
#             continue
#         print(i,j)

"""WHILE loop"""
# i = 1
# while i < 16:
#     if i == 11:
#         break
#     print(i)
#     i += 2
#
# print("out of the loop")

# i = 2
# while i <= 10:
#     if i == 6:
#         i = i+2
#         continue
#     print(i)
#     i +=2

# i = 4
# while i <= 28:
#     if i == 20:
#         i = i+4
#         continue
#     print(i)
#     i +=4
# print("COMPLETED")
#

i=0
while i <= 2:
    j = 0
    while j <= 2:
        if j == 1:
            j+=1
            continue
        print(i,j)
        j += 1
    i +=1