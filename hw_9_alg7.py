# Home Work 9 - Algorithm 7

# from random import randint
# from math import floor
#
#
# def get_random_list(length: int):
#     return [randint(-1000, 1000) for i in range(length)]

# Buit-in sort

# list1 = get_random_list(20)
# list1.sort(reverse=True)
# print(list1)


# Selection Sort

# def selection_sort(array: list):
#     i = 0
#     while i < len(array):
#         min_index = i
#         j = i + 1
#         while j < len(array):
#             if array[min_index] > array[j]:
#                 min_index = j
#             j += 1
#         array[i], array[min_index] = array[min_index], array[i]
#         i += 1
#     return array

# a = get_random_list(20)
# print(f'Input {a}')
# result = selection_sort(a)
# print(f'Output {result}')


# Bubble sort

# def bubble_sort(array: list):
#     i = 0
#     is_swap = False
#     while i < len(array):
#         j = 0
#         while j < (len(array) - 1 - i):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#             j += 1
#         if not is_swap:
#             break
#         i += 1
#     return array

# a = get_random_list(20)
# print(f'Input {a}')
# result = bubble_sort(a)
# print(f'Output {result}')


# Insertion sort

# def insertion_sort(array: list):
#     i = 0
#     while i < len(array):
#         j = i - 1
#         temp = array[i]
#         while array[j] > temp and j >= 0:
#             array[j + 1] = array[j]
#             j -= 1
#         array[j + 1] = temp
#         i += 1
#     return array


# a = get_random_list(20)
# print(f'Input {a}')
# result = insertion_sort(a)
# print(f'Output {result}')


# Merge sort

# def merge(left: list, right: list):
#     res = []
#     i, j = 0, 0
#     while i < len(left) or j < len(right):
#         if i == len(left):
#             res.append(right[j])
#             j += 1
#             continue
#         if j == len(right):
#             res.append(left[i])
#             i += 1
#             continue
#         if left[i] <= right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# def merge_sort(array: list):
#     if len(array) <= 1:
#         return array
#     middle = floor(len(array) / 2)
#     return merge(
#         merge_sort(array[:middle]),
#         merge_sort(array[middle:])
#     )
#
# a = get_random_list(20)
# print(f'Input {a}')
# result = merge_sort(a)
# print(f'Output {result}')


# Quick sort
#
# def quick_sort(array: list):
#     if len(array) <= 1:
#         return array
#     pivot = choice(array)
#     smaller = []
#     equal = []
#     greater = []
#
#     for item in array:
#         if item < pivot:
#             smaller.append(item)
#         elif item == pivot:
#             equal.append(item)
#         else:
#             greater.append(item)
#     return quick_sort(smaller) + equal + quick_sort(greater)
#
# a = get_random_list(20)
# print(f'Input {a}')
# result = quick_sort(a)
# print(f'Output {result}')


#  Linear search

# def linear_search(array: list, needed_item):
#     for i in array:
#         if i == needed_item:
#             return True
#     return False
#     index = 0
#     while index < len(array):
#         if array[index] == needed_item:
#             return index
#         index += 1
#     return -1


# Binary search
#
# def binary_search(array: list, needed_item):
#     first = 0
#     last = len(array) - 1
#     found = False
#     while first <= last and not found:
#         mid = floor((first + last) / 2)
#         if needed_item == array[mid]:
#             found = True
#         elif needed_item < array[mid]:
#             last = mid - 1
#         elif needed_item > array[mid]:
#             first = mid + 1
#     return found
#
#
# a = get_random_list(20)
# print(f'Input {a}')
# result = binary_search(a, 34)
# print(f'Output {result}')

# 3. Codewars
# Kata 1 - Human Readable Time (https://www.codewars.com/kata/52685f7382004e774f0001f7)
# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)

# Example:
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59

# My Solution

# def make_readable(seconds):
#     hrs = 0
#     min = 0
#     sec = 0
#     if seconds < 60:
#         sec = seconds
#     elif seconds < 3600:
#         min = seconds // 60
#         sec = seconds % 60
#     else:
#         hrs = seconds // 3600
#         min = (seconds - (hrs * 3600)) // 60
#         sec = seconds % 60
#     if hrs < 10:
#         hrs = '0' + str(hrs)
#     else:
#         hrs = str(hrs)
#     if min < 10:
#         min = '0' + str(min)
#     else:
#         min = str(min)
#     if sec < 10:
#         sec = '0' + str(sec)
#     else:
#         sec = str(sec)
#
#     return f'{hrs}:{min}:{sec}'
