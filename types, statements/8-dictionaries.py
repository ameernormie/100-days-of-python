student = {
    "name": 'ameer',
    "id": 123,
    "feedback": None
}

print(student["name"])  # ameer
# print(student["unknown-key"])       # KEY ERROR

# If key is not found `Unknown` will be printed
print(student.get('unknown-key', 'Unknown'))


student.keys()                # ['name', 'id', 'feedback']
student.values()                # ['ameer', 123, None]
