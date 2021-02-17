# 1. Sum digits up from a n number
#
# n = input("Enter a number greater than 0: ")
# sum_n = 0
# if int(n) > 0:
#     for i in n:
#         sum_n += int(i)
# else:
#     print('The number you entered is not greater than 0 please try again :)')
#
# print(sum_n)


# 2. Find max number
#
# a = int(input('Introduce number one: '))
# b = int(input('Introduce number two: '))
# c = int(input('Introduce number three: '))
# max_n = a
#
# if b > a:
#     max_n = b
# if c > b:
#     max_n = c
#
# print(f'The number {max_n} is the biggest of all introduced.')


# 3. Count odd and even numbers
#
# num = input('Introduce a number: ')
# odd_count = 0
# even_count = 0
#
# if int(num) < 0:
#     num = abs(int(num))
# for i in str(num):
#     if int(i) % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print(f'The introduced number {num} has {odd_count} odd digits and {even_count} even digits')
