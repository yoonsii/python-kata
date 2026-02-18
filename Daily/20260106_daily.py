def header():
    print("*******************************")

mylist = [1,2,5,15,20,2,23,12,5,3,6]

# # for i in mylist:
# #     if i % 2 == 0:
# #         print(i)

#  # count how many numbers are greater than 10
#  # 

# count = 0

# for i in mylist:
#     if i > 10:
#         count = count + 1

# print(count)

# #alternatively

# print(len([i for i in mylist if i > 10]))

# header()


# # sum all numbers divis by 6
# print(sum([i for i in mylist if i % 3 == 0]))

# header()

# # Print "Fizz" if number is divisible by 3, "Buzz" if by 5, or the number otherwise.

# for i in mylist:
#     if i % 3 == 0 :
#         print("Fizz")
#     if i % 5 == 0 :
#         print("Buzz")
#     else:
#         print(i)  

# header()

# #Find the smallest number in a list (without min()).

# min = mylist[0]

# for i in mylist:
#     if i < min:
#         min = i
# print(min)

# ## commenting out section 1 to move onto theme 2

# Focus: Defining and calling functions, return values, parameters.

# Write a function that returns the square of a number
# Write a function that takes two numbers and returns the larger
# Write a function that checks if a number is even
# Write a function that adds all numbers in a list
# Write a function that returns a list of all odd numbers from a list.

# def sq(x):
#     return pow(x,2)

# print(sq(2))

# header()

# def maximum(x,y):
#     if x == 0 and y == 0:
#         print("both num 0")
#         return # need to learn error handling
#     return max(x,y)

# print(maximum(0,0))

# def is_even(x):
#     return x % 2 == 0

# def sum_list(l):
#     return sum(l)


# print(sum_list(mylist))

# def get_odd_from_list(l):
#     return [x for x in l if x % 2 != 0]

# print(get_odd_from_list(mylist))

# Focus: Indexing, slicing, list comprehensions, string basics.

# Get the first 3 elements of a list
# Reverse a string
# Replace all "a"s with "@" in a string
# Capitalize the first letter of each word in a sentence
# Build a list of squares using list comprehension.

def get_three(l):
    if len(l) > 2:
        return [l[0],l[1],l[2]]

print(get_three(mylist))


reverse_string = "I love my baba. Be good to her"
new_string = ""

for i in range(len(reverse_string)-1,-1,-1):
    new_string += reverse_string[i]

print(new_string)

old_string = "have a banana"
new_string = ""

# new_string = [i for i in range(len(old_string)-1))] # was trying to do this with comprehension but got stuck

for i in range(len(old_string) - 1):
    if old_string[i] == "a":
        new_string += "@"
    else:
        new_string += old_string[i]

print(new_string)

cap_string = "I love my baba. Be good to her"
new_string = []

for word in cap_string.split():
    print(word)
    new_string.append(word.capitalize())

output = " ".join(new_string)
print(output)



