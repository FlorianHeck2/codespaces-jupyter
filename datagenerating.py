from faker import Faker
import random

fake = Faker()
#print(fake.name())

students = []

for _ in range(10):
    student = {
        "name": fake.name(),
        "age":random.randint(18, 25),
        "major":random.choice(["Computer Science", "Mathematics", "Physics"]),
        "gpa":round(random.uniform(2.0, 4.0),2),
        "is_international":random.choice([True, False])
    }
    students.append(student)

first_names = []
    
for student in students:
    full_name = student["name"]
    first_name = full_name.split()[0]
    last_name = full_name.split()[1]
    #print(first_name, last_name)
    first_names.append(first_name)

teststudent = students[8]
#print(teststudent["age"])

def duplicate_Checker(toCompare):
    storelist = []
    for attribute in toCompare:
        storelist


