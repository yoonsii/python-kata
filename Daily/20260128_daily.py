# Theme 1: Working with Collections 
from collections import Counter


# Focus: advanced list/dict/set operations, frequency counts, nested structures 
#     Write a function that returns the top 2 most common elements in a list. 

my_list = {1,2,5,3,2,2,4,5,6,4,2,2,1}

def most_common_two(l):
    return Counter(l).most_common(2)

print(most_common_two(my_list))

#     Remove duplicates from a list but preserve the original order. 
# [x for i, x in enumerate(l) if x not in l[:i]] 
#     Flatten a 2D list: [[1,2],[3,4]] → [1,2,3,4]. 
#     Given a list of words, return a dict of word lengths. 
# word_lengths = {word: len(word) for word in word_list} 
#     Given a list of dicts with "name" and "age", return the oldest person’s name. 

 
 

# Theme 2: String Patterns & Cleanup 

# Focus: string parsing, cleanup, slicing, and basic regex-like logic 
#     Normalize a sentence: remove leading/trailing space, lowercase, and ensure it ends in a period. 
#     Replace all digits in a string with "X" (no re module yet). 
#     Extract the username from an email string like "user@example.com". 
#     Count how many times each character appears in a string. 
#     Check if two strings are anagrams (e.g. "listen" and "silent"). 

 
 

# Theme 3: Defensive Coding & Logic 

# Focus: safe inputs, error handling, booleans, and guard clauses 
#     Write a function that divides two numbers, but returns "invalid" if dividing by 0. 
#     Write a function that returns True only if input is a non-empty list of integers. 
#     Given a list of dicts with optional "score" keys, return average score (skip if missing). 
#     Write a function that checks if a password is strong (8+ chars, has digit, has upper/lower). 
#     Return "OK" if string length is between 3 and 10, otherwise "Too short" or "Too long". 