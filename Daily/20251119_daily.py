for i in range(0,10):
    print(i)


def add_num(a,b):
    return a+b


print(add_num(10,20))


# Use enumerate() to print each item and its index from a list of fruits. 
# Use zip() to combine two lists (names and scores) and print them like "Alice scored 93" 
# Loop through numbers 1–20 and print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for both. 
# Write a loop that prints a square (5x5) of alternating # and . characters like a checkerboard. 

fruits = ['apple','banana','cherry','durian']

for i,fruit in enumerate(fruits):
    print(f"{i} and {fruit}")

names = ["hannah","steven","obo"]
scores = [12,54,100]

for combined in zip(names,scores):
    print(combined)

for i in range(1,21):
    print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 5 == 0:
        print("Buzz")
    if i % 3 == 0:
        print("Fizz")


for i in range (5):
    for j in range(5):
        if (i+j) % 2 == 0:
            print("#")
        else:
            print(".")
     



# Theme: Arguments, return values, and reusability 


# Write a function multiply_or_add(x, y, *, op='multiply') that multiplies or adds based on the keyword argument. 
# Write a function describe_person(name, age, city="Unknown") that returns a string like "Alice is 30 and lives in Tokyo". 
# Write a function min_max_avg(lst) that returns the min, max, and average as a tuple. 
# Write a function apply_to_all(func, lst) that applies a function to every element in a list and returns the result list. 

 

# Theme: Filtering, transformation, and complexity 

 

# Create a list of the squares of all even numbers between 1 and 20 using list comprehension. 
# Create a list of all 3-letter words from ["cat", "apple", "dog", "banana", "ant"] using a list comprehension. 
# Build a dictionary using dict comprehension where keys are numbers 1–5 and values are their cubes. 
# Use list comprehension to flatten [[1,2,3],[4,5],[6]] into [1,2,3,4,5,6] 