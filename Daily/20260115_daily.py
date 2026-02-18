from collections import Counter
# Write a function that returns the top 2 most common elements in a list. 

list_nums = [2,3,1,3,6,3,5,3,6,4,3,2,3,4,2,1,4,2]

# def two_common(l):
#     return Counter(l).most_common(2)

# print(two_common(list_nums))

# # Remove duplicates from a list but preserve the original order. 

# def remove_dups(l):
#     seen = set()
#     output = []
#     for i in l:
#         if not i in seen:
#             seen.add(i)
#             output.append(i)
#     return output

# print(remove_dups(list_nums))



# # Flatten a 2D list: [[1,2],[3,4]] → [1,2,3,4]. 
# my_list = [[1,2],[3,4]]

# x = [y for x in my_list for y in x]

# print(x)


# # Given a list of words, return a dict of word lengths. 

# word_list = ["here", "is", "a", "list", "of", "words"]

# word_lengths = {}

# for word in word_list:
#     word_lengths[word] = len(word)

# print(word_lengths)


# # Given a list of dicts with "name" and "age", return the oldest person’s name. 

# people = [
#     {"name": "keshan", "age": 36},
#     {"name": "baba", "age": 32},
#     {"name": "Jason", "age": 35}
# ]

# max_age = 0
# max_name = ""

# for person in people:
#     if person["age"] > max_age:
#         max_age = person["age"]
#         max_name = person["name"]

# print(f"{max_name}")
# Normalize a sentence: remove leading/trailing space, lowercase, and ensure it ends in a period. 

def normalise(s):
        s = s.lower().strip()
        return s if s[len(s) - 1] == "." else s + "."

print(normalise("JHi sdfji sdf"))

# Replace all digits in a string with "X" (no re module yet). 
def replace_digit(s):
    return "".join("X" if i.isdigit() else i for i in s)

print(replace_digit("sdf232f2324sfs31oklj1"))

# Extract the username from an email string like "user@example.com". 
def extract_username(s):
      return s.split("@")[0]

print(extract_username("test@balllll.com"))

# Count how many times each character appears in a string. 
def count_chars(s):
      return Counter(list(s))

print(count_chars("this is a sentenct"))

# Check if two strings are anagrams (e.g. "listen" and "silent").

def anagrams(s1,s2):
      return sorted(s1) == sorted(s2)

print(anagrams("listen","silsent"))



    Write a function that divides two numbers, but returns "invalid" if dividing by 0. 

    Write a function that returns True only if input is a non-empty list of integers. 

    Given a list of dicts with optional "score" keys, return average score (skip if missing). 

    Write a function that checks if a password is strong (8+ chars, has digit, has upper/lower). 

    Return "OK" if string length is between 3 and 10, otherwise "Too short" or "Too long". 0