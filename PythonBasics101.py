'''Introduction to Python -Syntaxt,Variables , data types '''

# print( Welcome to the GPA calculator. )
# print(Please enter all your letter grades, one per line.)
# print(Enter a blank line to designate the end.)
# # map from letter grade to point value
# points = { A+ :4.0, A :4.0, A- :3.67, B+ :3.33, B :3.0, B- :2.67,
# C+ :2.33, C :2.0, C :1.67, D+ :1.33, D :1.0, F :0.0}
# num courses = 0
# total points = 0
# done = False
# while not done:
# grade = input( ) # read line from user
# if grade == : # empty line was entered
# done = True
# elif grade not in points: # unrecognized grade entered
# print("Unknown grade {0} being ignored".format(grade))
# else:
# num courses += 1
# total points += points[grade]
# if num courses > 0: # avoid division by zero
# print( Your GPA is {0:.3} .format(total points / num courses))

#Simple solution
print('Welcome to the GPA calculator.')

# Prompt the user to enter their letter grades
grade1 = input('Please enter your first letter grade: ')
grade2 = input('Please enter your second letter grade: ')
grade3 = input('Please enter your third letter grade: ')

# Map letter grades to their corresponding point values
A_PLUS = 4.0
A = 4.0
A_MINUS = 3.67
B_PLUS = 3.33
B = 3.0
B_MINUS = 2.67
C_PLUS = 2.33
C = 2.0
C_MINUS = 1.67
D_PLUS = 1.33
D = 1.0
F = 0.0

# Calculate total points and number of courses
num_courses = 0
total_points = 0

# Process each grade and calculate GPA
def calculate_gpa(grade):
    global num_courses
    global total_points
    if grade == 'A+':
        total_points += A_PLUS
    elif grade == 'A':
        total_points += A
    elif grade == 'A-':
        total_points += A_MINUS
    elif grade == 'B+':
        total_points += B_PLUS
    elif grade == 'B':
        total_points += B
    elif grade == 'B-':
        total_points += B_MINUS
    elif grade == 'C+':
        total_points += C_PLUS
    elif grade == 'C':
        total_points += C
    elif grade == 'C-':
        total_points += C_MINUS
    elif grade == 'D+':
        total_points += D_PLUS
    elif grade == 'D':
        total_points += D
    elif grade == 'F':
        total_points += F
    else:
        print("Unknown grade {0}".format(grade))
        return
    num_courses += 1

calculate_gpa(grade1)
calculate_gpa(grade2)
calculate_gpa(grade3)

# Calculate GPA and print the result
if num_courses > 0:
    print('Your GPA is {0:.3}'.format(total_points / num_courses))


print('Welcome to the GPA calculator.')
grade = input('Please enter all your letter grades, one per line\n') #not how the while loop behaves
# print('Please enter all your letter grades, one per line\n')
print('Enter a blank line to designate the end.')

# map from letter grade to point value
points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
          'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

num_courses = 0
total_points = 0
done = False

while not done:
    # grade = input()  # read line from user
    if grade == '':  # empty line was entered
        done = True
    elif grade not in points:  # unrecognized grade entered
        print("Unknown grade {0} being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0:  # avoid division by zero
    print('Your GPA is {0:.3}'.format(total_points / num_courses))



'''
Changes made:

Enclosed dictionary keys in quotes to make them strings: 'A+', 'A', 'A-', ....
Changed variable names to adhere to Python conventions: num_courses, total_points.
Fixed the if condition for checking an empty line: if grade == ''.
Fixed syntax error in the GPA print statement: print('Your GPA is {0:.3}'.format(total_points / num_courses)).


'''

#Same problem using for Loop 

print('Welcome to the GPA calculator.')
print('Please enter all your letter grades, one per line')
print('Enter a blank line to designate the end.')

points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
          'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

num_courses = 0
total_points = 0

for grade in iter(input, ''):
    if grade not in points:
        print("Unknown grade {0} being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]

if num_courses > 0:
    print('Your GPA is {0:.3}'.format(total_points / num_courses)) 