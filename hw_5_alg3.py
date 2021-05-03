# Home Work 5 - Algorithm 3

# 1. Recursion for Fibonacci
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(2))
#
#
#
# 2. Recursion for factorial
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print((factorial(6)))
#
#
#
# 3. Recursion for digital root
#
# def digital_root(n):
#     if n < 10:
#         return n
#     else:
#         return digital_root(n % 10 + digital_root(n // 10))
#
# print(digital_root(233))



# 4. codewars.com


# Kata 1 - Is this a triangle? (https://www.codewars.com/kata/56606694ec01347ce800001b)
# Implement a method that accepts 3 integer values a, b, c.
# The method should return true if a triangle can be built with the sides of given length and false in any other case.

# My solution

# def is_triangle(a, b, c):
#     if (a < 1) or (b < 1) or c < 1:
#         return False
#     else:
#         if (a + b <= c) or (a + c <= b) or (b + c <= a):
#             return False
#         else:
#             return True


# Kata 2 - Scramblies (https://www.codewars.com/kata/55c04b4cc56a697bb0000048)
# Complete the function scramble(str1, str2) that returns true
# if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

# My solution

# def scramble(s1, s2):
#     for c in set(s2):
#         if s1.count(c) < s2.count(c):
#             return False
#     return True



# 5. Write a function to check if a number is Perfect or not
#
# def perfect_num(n):
#     sum = 0
#     for i in range(1, n):
#         if n % i == 0:
#             sum += i
#     return sum == n
#
# print(perfect_num(6))



# 6. Amicable numbers from slides
#
# def find_divisors(n):
#     div = set()
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             div.add(i)
#             div.add(int(n//i))
#     return list(div)
#
#
# def amicable_num(n1, n2):
#     div_n1 = sum(find_divisors(n1)) - n1
#     div_n2 = sum(find_divisors(n2)) - n2
#     return n1 == div_n2 and n2 == div_n1
#
#
# print(find_divisors(220))
# print((find_divisors(284)))
#
# print(sum(find_divisors(220)))
# print(sum(find_divisors(284)))
#
# print(amicable_num(220, 284))