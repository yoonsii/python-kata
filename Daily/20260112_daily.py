print("hello world")

#Write a function that divides two numbers, but returns "invalid" if dividing by 0.
def divide(n,d):
    if d == 0:
        raise Exception("Cannot divide by zero")
    else:
        return (n/d)
    
print(divide(10,5))
#print(divide(10,0))

#Write a function that returns True only if input is a non-empty list of integers.
def check_list(l):
    if not l or not isinstance(l,list):
        return False
    else:
        for item in l:
            if not isinstance(item,int):
                return False
        return True


#Given a list of dicts with optional "score" keys, return average score (skip if missing).
students = [
    {"name":"keshan","score":25},
    {"name":"bob","score":100},
    {"name":"baba",}
]

print(students[0]["name"])

def average_score(l):
    score = 0
    count = 0
    for item in l:
        if "score" in item:
            score += item["score"]
            count += 1
    return (score / count)

print(average_score(students))
#Write a function that checks if a password is strong (8+ chars, has digit, has upper/lower).

def check_pw(s):

    has_digit = False
    has_upper = False
    has_lower = False

    if len(s) < 8:
        return False
    
    for c in s:
        if c.isdigit():
            has_digit = True
            break
    
    for c in s:
        if c in "abcdefghijklmnopqrstuvwxyz":
            has_lower = True
            break
    
    for c in s:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            has_upper = True
            break
    
    return has_digit and has_lower and has_upper
    

print(check_pw("hel234lo")) 

#Return "OK" if string length is between 3 and 10, otherwise "Too short" or "Too long".

str_len = "this is a string"

def check_strr():
    if str_len <= 10 and str_len >= 3:
        return "OK"
    elif str_len < 3:
        return "Too Short"
    elif str_len > 10:
        return "Too Long"
