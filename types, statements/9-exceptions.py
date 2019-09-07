student = {
    "name": 'ameer',
    "id": 123,
    "feedback": None
}

try:
    last_name = student['last-name']               # ['ameer', 123, None]
except KeyError:
    print('Error finding last name')

print('this code executes')


student['last-name'] = 'hamza'
try:
    last_name = student['last-name']
    numbered_last_name = 3 + last_name             # ['ameer', 123, None]
except KeyError:
    print('Error finding last name')
except TypeError as error:                          # This will tell the error and you can print it out
    print('Type error caught')
    print(error)
except Exception:
    print('All type of exception handled')

print('this code executes')
