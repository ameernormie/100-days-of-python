student_names = ['ameer', 'hamza', 'talha', 'ali',
                 'saad', 'qadeer', 'ehsan', 'haris', 'hasan']

for name in student_names:
    if name is 'ali':
        print('found ameer')
        break                               # exits when finds the element
    print('currently testing')

# execute for every element of list except for `haris`
for name in student_names:
    if name is 'haris':
        continue
        print('found haris')                # will not be executed
    print('curren tly testing ' + name)
