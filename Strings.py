course = 'python for beginners'
another = course[:]
print(another)

name = 'Jennifer'
print(name[1:-1])

#formatted strings#
first = 'Woohyuk'
last = 'Lee'
message = first + ' [' + last + '] is a Coder' 
print(message)
msg = f'{first} [{last}] is a Coder' #formatted string#
print(msg)

#string methods#
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course)
print(course.lower())
print(course.find('for'))
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('o', 'OOO'))
print('Python' in course)