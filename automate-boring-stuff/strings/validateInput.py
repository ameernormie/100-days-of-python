while True:
    print('What is your age?')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a valid age')

while True:
    print('Select a new password (letter and numbers only)')
    password = input()
    if password.isalnum():
        break;
    print('passwords can only contain letters and numbers')


