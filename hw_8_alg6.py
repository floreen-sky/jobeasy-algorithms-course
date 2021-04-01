# Home Work 8 - Algorithm 6


# 1. Find the biggest number in the list (divide and rule).


# arr = list(map(int, input("Enter the elements of the list separated by space: ").strip().split()))


# def find_max_dac(a, low, high):
#     if len(a) == 0:
#         return f'Your array is empty'
#     if len(a) == 1:
#         return a[0]
#     if low >= high - 2:
#         if a[low] > a[low + 1]:
#             return a[low]
#         else:
#             return a[low + 1]
#
#     rez = find_max_dac(a, low + 1, high)
#
#     if a[low] > rez:
#         return a[low]
#     else:
#         return rez


# This solution uses binary search


# def find_max_dac(a, low, high):
#     if len(a) == 0:
#         return f'Your array is empty'
#     if len(a) == 1:
#         return a[0]
#     mid = (low + high) // 2
#     if low == high - 2 or low == mid - 1:
#         if a[low] > a[low + 1]:
#             return a[low]
#         else:
#             return a[low + 1]
#     else:
#         rez1 = find_max_dac(a, low, mid)
#         rez2 = find_max_dac(a, mid + 1, high)
#
#     if rez1 > rez2:
#         return rez1
#     else:
#         return rez2


# print("The maximum number in the entered list", arr, "is : ", find_max_dac(arr, 0, len(arr)))

################################################

# 2. Codewars
# Kata #1 - Find The Parity Outlier (https://www.codewars.com/kata/5526fc09a1bbd946250002dc)
# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers
# except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

# Examples:
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

# My solution

# def find_outlier(integers):
#     count_even = 0
#     count_odd = 0
#     result = 0
#     for i in range(3):
#         if integers[i] % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     if count_even > count_odd:
#         for i in integers:
#             if i % 2 != 0:
#                 result = i
#     else:
#         for i in integers:
#             if i % 2 == 0:
#                 result = i
#
#     return result

###################################

# Kata #2 Delete occurrences of an element if it occurs more than n times

# Description see https://www.codewars.com/kata/554ca54ffa7d91b236000023

# Example:
# delete_nth([1, 1, 1, 1], 2)  # return [1,1]
# delete_nth([20, 37, 20, 21], 1)  # return [20,37,21]

# My Solution

# def delete_nth(order,max_e):
#     order2 = order[::-1]
#     for i in order2:
#         c = order2.count(i)
#         if c > max_e:
#             x = c - max_e
#             while x != 0:
#                 order2.remove(i)
#                 x -= 1
#     return order2[::-1]
