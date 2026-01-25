from collections import Counter
# 20260112_daily kata - repeating same themes to improve and drill

# #theme one
# Write a function that returns the top 2 most common elements in a list.
mylist = [1,2,7,3,4,5,3,2,4,5,1,2,3,4,1,1]

def most_common(l):
    return Counter(l).most_common(2)

print(most_common(mylist))

# Remove duplicates from a list but preserve the original order.

def remove_duplicates_with_preserve(l):
    seen = set()
    output = []
    for item in l:
        if item not in seen:
            output.append(item)
            seen.add(item)
    return output

print(remove_duplicates_with_preserve(mylist))
        


# Flatten a 2D list: [[1,2],[3,4]] → [1,2,3,4].
# Given a list of words, return a dict of word lengths.
# Given a list of dicts with "name" and "age", return the oldest person’s name.