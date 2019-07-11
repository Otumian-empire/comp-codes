# # implementing a merge sort algo

# my_list = [2, 1, 3, 6, 8, 2, 3, 0]

# s_my_list = len(my_list)

# my_new_list = []

# list_a = []
# list_b = []

# if (s_my_list % 2 == 0):
#     list_a = my_list[0 : int(s_my_list/2)]
# else:
#     list_a = my_list[0 : int(s_my_list/2) + 1]

# list_b = my_list[int(s_my_list/2):]

# a = 1
# b = 1

# for i in range(1, s_my_list - 1):
#     print("a = ", a, "b = ", b, "i = " ,i)
#     if list_a[a] < list_b[b]:
#         my_new_list.append(list_a[a])
#         a += 1
#     else:
#         my_new_list.append(list_b[b])
#         b += 1

# print("The original list", my_list)
# print("The new list", my_new_list)


# # for i in range(s_my_list):
# #     print("a = ", a, "b = ", b, "i = " ,i)
# #     if list_a[a] < list_b[b ]:
# #         my_new_list.append(list_a[a])
# #         a += 1
# # print(my_new_list)