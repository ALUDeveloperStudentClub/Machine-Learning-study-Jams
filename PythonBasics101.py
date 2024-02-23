# '''Introduction to Python -Syntaxt,Variables , data types '''

# # Group One :

# # total_credits=input("Enter total credits:")
# # total_hours=input("Enter total hours you spent in class:")
# # gpa=float(total_credits)/float(total_hours)
# # print("your gpa is:",gpa)


# # simple GPA calculator in python
# # def gpa_cal():
    
# #     tot = int(input("Enter the number of subjects: "))
# #     marks = []
# #     credits = []
# #     total = []
# #     for i in range(tot):
# #         marks.append(float(input("Enter the marks: ")))
# #         credits.append(float(input("Enter the Credits: ")))
# #         total.append(marks[i] * credits[i])
        
# #     gpa = (sum(total)/sum(credits) * 4)/100
        

# #     print(f"GPA is {gpa:.1f}")
# # gpa_cal()
# # print("\nThis is GPA Calculator\n")

# # math = input("Enter your math grade in this format (x/y): ")
# # chem = input("Enter your chemistry grade in this format (x/y): ")
# # bio = input("Enter your biology grade in this format (x/y): ")
# # eng = input("Enter your english grade in this format (x/y): ")

# # math = math.split("/")
# # math_yabonye = int(math[0])
# # math_yakoreyeho = int(math[1])

# # if math_yabonye > math_yakoreyeho:
# #     print("Your math grade is higher than your Total grade")
# #     exit()

# # chem = chem.split("/")
# # chem_yabonye = int(chem[0])
# # chem_yakoreyeho = int(chem[1])
# # if chem_yabonye > chem_yakoreyeho:
# #     print("Your chemistry grade is higher than your Total grade")
# #     exit()
    

# # bio = bio.split("/")
# # bio_yabonye = int(bio[0])
# # bio_yakoreyeho = int(bio[1])
# # if bio_yabonye > bio_yakoreyeho:
# #     print("Your biology grade is higher than your Total grade")
# #     exit()

# # eng = eng.split("/")
# # eng_yabonye = int(eng[0])
# # eng_yakoreyeho = int(eng[1])
# # if eng_yabonye > eng_yakoreyeho:
# #     print("Your english grade is higher than your Total grade")
# #     exit()

# # sum_yabonye = math_yabonye + chem_yabonye + bio_yabonye + eng_yabonye
# # sum_yakoreyeho = math_yakoreyeho + chem_yakoreyeho + bio_yakoreyeho + eng_yakoreyeho

# # percent = sum_yabonye * 100 / sum_yakoreyeho

# # gpa = percent * 4 / 100

# # print("Your GPA is: " + str(gpa) )

# # A

# # # print( Welcome to the GPA calculator. )
# # # print(Please enter all your letter grades, one per line.)
# # # print(Enter a blank line to designate the end.)
# # # # map from letter grade to point value
# # # points = { A+ :4.0, A :4.0, A- :3.67, B+ :3.33, B :3.0, B- :2.67,
# # # C+ :2.33, C :2.0, C :1.67, D+ :1.33, D :1.0, F :0.0}
# # # num courses = 0
# # # total points = 0
# # # done = False
# # # while not done:
# # # grade = input( ) # read line from user
# # # if grade == : # empty line was entered
# # # done = True
# # # elif grade not in points: # unrecognized grade entered
# # # print("Unknown grade {0} being ignored".format(grade))
# # # else:
# # # num courses += 1
# # # total points += points[grade]
# # # if num courses > 0: # avoid division by zero
# # # print( Your GPA is {0:.3} .format(total points / num courses))

# # #Simple solution
# # print('Welcome to the GPA calculator.')

# # # Prompt the user to enter their letter grades
# # grade1 = input('Please enter your first letter grade: ')
# # grade2 = input('Please enter your second letter grade: ')
# # grade3 = input('Please enter your third letter grade: ')

# # # Map letter grades to their corresponding point values
# # A_PLUS = 4.0
# # A = 4.0
# # A_MINUS = 3.67
# # B_PLUS = 3.33
# # B = 3.0
# # B_MINUS = 2.67
# # C_PLUS = 2.33
# # C = 2.0
# # C_MINUS = 1.67
# # D_PLUS = 1.33
# # D = 1.0
# # F = 0.0

# # # Calculate total points and number of courses
# # num_courses = 0
# # total_points = 0

# # # Process each grade and calculate GPA
# # def calculate_gpa(grade):
# #     global num_courses
# #     global total_points
# #     if grade == 'A+':
# #         total_points += A_PLUS
# #     elif grade == 'A':
# #         total_points += A
# #     elif grade == 'A-':
# #         total_points += A_MINUS
# #     elif grade == 'B+':
# #         total_points += B_PLUS
# #     elif grade == 'B':
# #         total_points += B
# #     elif grade == 'B-':
# #         total_points += B_MINUS
# #     elif grade == 'C+':
# #         total_points += C_PLUS
# #     elif grade == 'C':
# #         total_points += C
# #     elif grade == 'C-':
# #         total_points += C_MINUS
# #     elif grade == 'D+':
# #         total_points += D_PLUS
# #     elif grade == 'D':
# #         total_points += D
# #     elif grade == 'F':
# #         total_points += F
# #     else:
# #         print("Unknown grade {0}".format(grade))
# #         return
# #     num_courses += 1

# # calculate_gpa(grade1)
# # calculate_gpa(grade2)
# # calculate_gpa(grade3)

# # # Calculate GPA and print the result
# # if num_courses > 0:
# #     print('Your GPA is {0:.3}'.format(total_points / num_courses))


# print('Welcome to the GPA calculator.')
# # grade = input('Please enter all your letter grades, one per line\n') #not how the while loop behaves
# print('Please enter all your letter grades, one per line\n')
# print('Enter a blank line to designate the end.')

# # map from letter grade to point value
# points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
#           'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

# num_courses = 0
# total_points = 0
# done = False

# while not done:
#     grade = input()  # read line from user
#     if grade == '':  # empty line was entered
#         done = True
#     elif grade not in points:  # unrecognized grade entered
#         print("Unknown grade {0} being ignored".format(grade))
#     else:
#         num_courses += 1
#         total_points += points[grade]

# if num_courses > 0:  # avoid division by zero
#     print('Your GPA is {0:.3}'.format(total_points / num_courses))



# # '''
# # Changes made:

# # Enclosed dictionary keys in quotes to make them strings: 'A+', 'A', 'A-', ....
# # Changed variable names to adhere to Python conventions: num_courses, total_points.
# # Fixed the if condition for checking an empty line: if grade == ''.
# # Fixed syntax error in the GPA print statement: print('Your GPA is {0:.3}'.format(total_points / num_courses)).


# # '''

# # #Same problem using for Loop 

# # print('Welcome to the GPA calculator.')
# # print('Please enter all your letter grades, one per line')
# # print('Enter a blank line to designate the end.')

# # points = {'A+': 4.0, 'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67,
# #           'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

# # num_courses = 0
# # total_points = 0

# # for grade in iter(input, ''):
# #     if grade not in points:
# #         print("Unknown grade {0} being ignored".format(grade))
# #     else:
# #         num_courses += 1
# #         total_points += points[grade]

# # if num_courses > 0:
# #     print('Your GPA is {0:.3}'.format(total_points / num_courses)) 

Benin = [ {"Name":"benin",
           "Age":2} , {"Name":"Khalid",
                       "Age": 4}]

print(Benin[0])