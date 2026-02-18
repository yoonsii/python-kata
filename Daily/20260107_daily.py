# Batch 1: String Manipulation & Formatting 

 

# Write a function clean_username(s) that strips leading/trailing spaces and lowercases the input. 
def clean_username(s):
    return s.strip().lower()

print(clean_username("   sSDWERrwr "))


# Write a function snake_to_title(s) that converts "hello_world_test" → "Hello World Test". 
def snake_to_title(s):
    return " ".join([word.capitalize() for word in s.split("_")])

print(snake_to_title("hello_world_test"))

# Write a loop that prints each word in "devops is discipline" with its index using enumerate(). 
mystring = "devops is discipline"

for i,word in enumerate(mystring.split()):
    print(f"Word: {word}, Index: {i}")
    
# Format this string using f-strings: name = "Keshin", role = "DevOps" → "Keshin is training as a DevOps warrior" 
name = "Keshan"
role = "DevOps" 

print(f"{name} is training as a {role} warrior!")
 

# Batch 2: Logic, Branching, and Realistic Thinking 

# Write a function classify_score(score) that returns: "fail" if <50, "pass" if <85, "distinction" if 85+. 
def classify_score(score):
    if score >= 85:
        return "distinction"
    elif score >= 50:
        return "pass"
    elif score < 50:
        return "fail"
    
print(classify_score(40))


# Write a function range_check(x) that returns True only if x is between 10 and 20 (inclusive). 
def range_check(x):
    return (x >= 10 and x <= 20)

print(range_check(222))

# Write a loop that finds the first number between 1 and 50 divisible by both 7 and 9. Use break. 

for i in range(1,200,1):
    if i % 7 == 0 and i % 9 == 0:
        print(i)
        break


# Write a function is_palindrome(s) that checks whether a string is a palindrome (e.g. "racecar"). 
def is_palindrome(s):
    reversed_s = s[::-1]
    return s == reversed_s

print(is_palindrome("racecar"))


# Batch 3: Data Structures – Sets, Tuples, and Dicts 

# Create a set from the list [1,2,2,3,4,4,5] and print it. 

mylist = [1,2,2,3,4,4,5]
print(set(mylist))


# Given person = ("Alice", 30, "Tokyo"), unpack it and print: "Alice is 30 and lives in Tokyo" 
person = ("Alice", 30, "Tokyo")
name, age, location = person

print(f"{name} is {age} and lives in {location}")

# Given a dict {"a": 1, "b": 2, "c": 3}, loop through its items and print key -> value 

d = {"a": 1, "b": 2, "c": 3}

for listing in d:
    print(f"{listing} -> {d[listing]}")


# Create a function invert_dict(d) that flips keys and values. 
# Input: {"a": 1, "b": 2} → Output: {1: "a", 2: "b"} 

def invert_dict(dd):
    output_dict = {}
    for listing in dd:
        print(f"{listing} -> {dd[listing]}")
        output_dict[dd[listing]] = listing
    return output_dict

print(invert_dict(d))

for key,value in d.items():
    print(f"{key}, {value}")