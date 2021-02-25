# 1. Fiboanacci
#
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(5))



# 2. Zeros not for Heroes
#
# n = int(input('Introduce a number: '))
#
#
# def no_zeros(n):
#     if n == 0:
#         return 0
#     while n % 10 == 0:
#         n //= 10
#     return n
#
#
# print(no_zeros(n))



# 3. Digital root is the recursive sum of all the digits in a number.
#
# def simplified_sum(n):
#     if n == 0:
#         return 0
#     elif n < 0:
#         n = abs(n)
#
#     # The next line of code is an alternative for summing the number starting with the first digit from the left :)
#     # rez = n // (10 ** (len(str(n))-1)) + sum_of_digit(n % (10 ** (len(str(n))-1)))
#
#     rez = n % 10 + simplified_sum(n // 10)
#     while rez > 9:
#         rez = simplified_sum(rez)
#     return rez
#
#
# n = 493193
# print(f'The simplified sum of {n} is {simplified_sum(n)}')
