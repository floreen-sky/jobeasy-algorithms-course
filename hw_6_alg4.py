# Home Work 6 - Algorithm 4

# 1. Enter a string of words separated by spaces. Find the longest word.

# def longest_word(words):
#     result = ''
#     for i in words.split():
#         if len(i) > len(result):
#             result = i
#     return result
#
# print(longest_word('Enter a string of words separated by spaces. Find the longest word'))



# 2. Irregular string to regular (delete all the unnecessary spaces between words and leave only one space.
# Delete also spaces before and after the entire string).

# def fix_string(string1):
#     return " ".join(string1.split())
#
# print(fix_string('Enter   a string of words    separated by spaces.'))



# 3. Count how many times a character (substring) is included in a string.

# def count_sbstr(string2, sbstr):
#     count = 0
#     sbstr_len = len(sbstr)
#     for i in range(len(string2)):
#         if string2[i:i+sbstr_len] == sbstr:
#             count += 1
#     return count
#
# print(count_sbstr('Count how many times a character (substring) is included in a string.', 'str'))



# 4. Find and replace a substring in a string for another substring.

# def replace_with_sbstr(string3, sbstr_old, sbstr_new):
#     rez = []
#     sbstr_old_len = len(sbstr_old)
#     for i in range(len(string3)):
#         if string3[i:i+sbstr_old_len] != sbstr_old:
#             rez += string3[i]
#         else:
#             rez.append(sbstr_new)
#     return ''.join(rez)
#
# print(replace_with_sbstr('Count how many times a character (substring) is included in a string.', 'str', '0000'))



# 5. Codewars
# Kata 1 - Stop gninnipS My sdroW! (https://www.codewars.com/kata/5264d2b162488dc400000001)
# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (like the name of this kata).

# My solution

# def spin_words(sentence):
#     new_sentence = ''
#     sentence_list = sentence.split()
#     for i in sentence_list:
#         if len(i) >= 5:
#             i = i[::-1]
#         new_sentence = f'{new_sentence} {i}'
#     return new_sentence[1:]


# Kata 2 - Jaden Casing Strings (https://www.codewars.com/kata/5390bac347d09b7da40006f6)

# My solution

# def to_jaden_case(string):
#     return " ".join(word.capitalize() for word in string.split())
