numbers = [1, 2, 3]

# typical way
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)

# list comprehension
new_list_2 = [n + 1 for n in numbers]
print(new_list_2)

# example 2
name = "Rajeshwaran"
letters = [letter for letter in name]
print(letters)

# challenge: double a range(1,5)
range_list = [item * 2 for item in range(1,5)]
print(range_list)

# conditional list comprehension
range_updated = [item * 2 for item in range(1, 10) if item % 2 == 0]
print(range_updated)

names = ["Alex", "Beth", "Akila", "Dhivya", "Priya", "Aram"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

# challenge: change the names to uppercase if the nane has more than 4 characters
another_name = ["Alex", "Beth", "Akila", "Dhivya", "Priya", "Aram"]
challenge_list = [name.upper() for name in another_name if len(name) > 4]
print(challenge_list)

# dictionary comprehension
import random
student_score = { name:random.randint(1, 100) for name in another_name }
print(student_score)

# conditional dictionary comprehension
passed_students = { key:value for (key, value) in student_score.items() if value >= 40 }
print(passed_students)

student_dict = {
    "student": [ 'Angela', 'James', 'Lily' ],
    "score": [56, 76, 98]
}
import pandas
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.student)