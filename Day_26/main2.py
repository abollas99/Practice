import random

import pandas

# list Comprehension
ages = [5, 7, 4, 10]
ages_5_years_later = [a + 5 for a in ages]

print(ages)
print(ages_5_years_later)

name = "Anthony"
name_list = [n for n in name]
print(name_list)

# challenge 1
numbers = [n * 2 for n in range(1, 5)]
print(numbers)

names = ["Alex", "Elanor", "Caroline", "Freddie", "Beth", "Dave"]
new_names = [n for n in names if len(n) >= 5]
print(new_names)

student_scores = {s:random.randint(1, 100) for s in names}
print(student_scores)

data = {
    'A' : [90, 93, 96, 99],
    'B' : [80, 83, 86, 89],
    'C' : [70, 73, 76, 79]
}
test = pandas.DataFrame(data)
print(test)
for (index, row) in test.iterrows():
    print(row)

