from collections import Counter
# Focus: advanced list/dict/set operations, frequency counts, nested structures

# Write a function that returns the top 2 most common elements in a list

# Flatten a 2D list: [[1,2],[3,4]] → [1,2,3,4].
# Given a list of words, return a dict of word lengths
# Given a list of dicts with "name" and "age", return the oldest person’s name.

mylist = [1,1,2,4,4,4,6,2,12,13,13,6,8,9,1]

# print(Counter(mylist))

# z = Counter(mylist)

# for i in z.items():
#     print(i)

#     # Thinking of a "traditional" way to do this

# for i,j in z.most_common(2):
#     print(i)

# # Remove duplicates from a list but preserve the original order
# # note: ok so we can't just turn it into a set..

# my_list = [1,7, 2, 3, 2, 1, 5, 6, 5,7, 5, 5]
# # Count element frequencies
# counts = Counter(my_list)

# # Filter for elements that appear more than once
# duplicates = [item for item, count in counts.items()]

# print(duplicates)

# #flatten a 2d list 

# list_2d = [[1,2],[3,4]]

# x = [j for x in list_2d for j in x]

# print(x)

# #Given a list of words, return a dict of word lengths.

# word_list = ['hello','this', 'is','a','wordlist']
# len_dict = {}

# for word in word_list:
#     len_dict[word] = len(word)

# print(len_dict)


# #Given a list of dicts with "name" and "age", return the oldest person’s name.

# people = [
#     {"name": "Alice", "age": 100},
#     {"name": "Bob", "age": 35},
#     {"name": "Charlie", "age": 22},
#     {"name": "Diana", "age": 41},
#     {"name": "Ethan", "age": 35},
# ]

# max_age = 0
# max_name = ""
# for item in people:
#     if item['age'] > max_age:
#         max_name = item['name']
#     print(item)

# print(max_name)

#THEME 2
# Theme 2: String Patterns & Cleanup

# Focus: string parsing, cleanup, slicing, and basic regex-like logic
# Normalize a sentence: remove leading/trailing space, lowercase, and ensure it ends in a period.
sentence = "  hello this ia cDFGg  "

def normalise(s):
    strip_lower = s.strip().lower()
    if strip_lower[len(strip_lower) - 1] != ".":
        return strip_lower + "."
    else:
        return strip_lower

print(normalise(sentence))

# Replace all digits in a string with "X" (no re module yet).

def undigit(s):
    return [c if c not in "0123456789" else "x" for c in s]

print("".join(undigit("Ths23l is 4 sent3nce")))

# Extract the username from an email string like "user@example.com".

def extract(s):
    return s.split("@")[0] 

print(extract("user@example.com"))

# Count how many times each character appears in a string.

def count_char(s):
    return Counter([c.lower() for c in s])

print(count_char(sentence))

# Check if two strings are anagrams (e.g. "listen" and "silent").

def anagram(s1,s2):
    return sorted(list(s1)) == sorted(list(s2))

print(anagram("listen","silent"))

# 🛡 Theme 3: Defensive Coding & Logic

# Focus: safe inputs, error handling, booleans, and guard clauses

# Write a function that divides two numbers, but returns "invalid" if dividing by 0.

def div(n,d):
    if d == 0:
        raise Exception("invalid")
    else: 
        return (n / d)


# Write a function that returns True only if input is a non-empty list of integers.

# a = []
# b = [1,4,5,"sdr"]
# def check_list(l):
#     if l:
#         for item in l:
#             if not int(item):
#                 return False
#         return True


# print(check_list(b))
#above not working try different tack

def check_list(l):
    if not isinstance(l,list) and not l:
        return False

    for item in l:
        if not isinstance(l,int):
            return False
    
    return True


# Given a list of dicts with optional "score" keys, return average score (skip if missing).

data1 = [
    {"name": "Alice", "score": 80},
    {"name": "Bob"},
    {"name": "Charlie", "score": 70},
    {"name": "Diana", "score": 90}
]

# Write a function that checks if a password is strong (8+ chars, has digit, has upper/lower).

# Return "OK" if string length is between 3 and 10, otherwise "Too short" or "Too long".