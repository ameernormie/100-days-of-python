student_names = ['ameer', 'hamza', 'talha']

student_names[0] == 'ameer'
student_names[1] == 'hamza'

# last value
student_names[-1] == 'talha'


# Add at the end

student_names.append('ali')             # ['ameer', 'hamza', 'talha', 'ali']

# Check if item is in the list
print('ameer' in student_names)

# Length of list
len(student_names)

# Delete element in list
del student_names[2]

print(student_names)                    # ['ameer', 'hamza', 'ali']

# List slicing
print(student_names[1:])                # ['hamza', 'ali']

# Print in reverse (Third argument is called the stepper)
print(student_names[::-1])              # 'ali', 'hamza', 'ameer']
