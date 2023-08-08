# from django.test import TestCase

# # # Create your tests here.
# def single_list(lst):
#     list1 = []
#     for item in lst:
#         if isinstance(item, list):
#             list1.extend(single_list(item))
#         else:
#             list1.append(item)
#     return list1

# # Example usage
# input_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# output_list = single_list(input_list)
# print(output_list) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# input_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
# list1 = []
# for item in input_list:
#         if isinstance(item, list):
#             list1.extend(item)
#         else:
#             list1.append(item)
# print(list1)

# list=[1,2,3,4,5,6,7,8,9]
# l1=[]
# l2=[]
# for i in list:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
    
# print(l1)
# print(l2)


# p='pushparaj'
# output=""
# for i in p:
#     output=i+output
# print(output)

l=[1,2,3,4,5,6]
list=0
for i in l:
    list=list+i
print(list)


    