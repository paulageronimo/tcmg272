# ______________________________________________________________________slide 1

integer = 0
string = "zero"
floating = 0.0
boolean  = False # BOOLEAN LOGIC: 0 - False, NO ; 1 - True, YES

print("integer", integer, "is a", type(integer))
print("string", string, "is a", type(string))
print("floating", floating, "is a", type(floating))
print("boolean", boolean, "is a", type(boolean))

# ______________________________________________________________________slide 2

# = : assigning it to a variable
examGrade = 74 # value of the examGrade

# == : comparisons (boolean)

perfectScore = (examGrade == 100) # inside value will give a BOOLEAN statement, true or false

print("My exam grade is a", examGrade) # will print out the value
print("I have a perfect score.", perfectScore) # will print out the Boolean value
# ______________________________________________________________________slide 3

# < : less than
negative = (examGrade < 0)
print("I have a negative grade.", negative)

# > : greater than
genius = (examGrade > 100)
print("I am a genius.", genius)

# <= : less than or equal to
failing = (examGrade <= 70)
print("I have a failing score.", failing)

# >= : greater than or equal to
passing = (examGrade >= 70)
print("I have a passing score.", passing)
# ______________________________________________________________________slide 4
# print("Tuesday" == "tuesday") # False due to the T
# print("2" < 3) # type error
# ______________________________________________________________________slide 5
# using = and == wrong, such as...
# examGrade == 74 # results in Error
# perfectScore == (examGrade = 100) # results in Error
# difference between operator and expression
# reference example in the slides
# ______________________________________________________________________slide 6
# and, or, not
previousExam = 95
passedPreviousExam = True
# and 
passedAllExams = passing and passedPreviousExam
# or
haveGrade =  passing or failing
print("I have passed all my exams.", haveGrade)
# not
positiveGrade = not negative
print("I have a valid grade.", positiveGrade)
# ______________________________________________________________________slide 7
# order of operations
# PEMDAS 
# common error: PARENTHESIS especially if PEMDAS
# ______________________________________________________________________slide 8
# if else
# refer to the flow chart
newExamGrade = 66
print("My final exam grade is a", newExamGrade)

if (examGrade >= 70):
    print("I passed my final exam.")
else:
    print("I failed my final exam.")

# ______________________________________________________________________slide 9
#multibranches and else if statements
if (newExamGrade >= 90):
    print("I got an A on my final exam.")
elif (newExamGrade >=80): #else, if (boolean)
    print("I got a B on my final exam.")
elif (newExamGrade >= 70):
    print("I got a C on my final exam.")
elif (newExamGrade >= 60):
    print("I got a D on my final exam.")
else:
    print("I got an F on my final exam.")
# ______________________________________________________________________slide 10
# nested if else
averageExamScore = (previousExam + examGrade + newExamGrade) / 3

if (averageExamScore >= 70):
    if (averageExamScore > 100): # genius = (examGrade > 100)
        print("I have a passing exam average, and I am a genius.")
    else:
        print("I have a passing exam average.")
    print("My average exam score is", averageExamScore)
else:
    if (newExamGrade >= 60):
        print("I got a D on my exam average.")
    elif (newExamGrade >= 0):
        print("I got an F on my exam average.")  
    else: # same as saying newExamAverage < 0
        print("I have a negative.")
    print("My average exam score is", averageExamScore)

# ______________________________________________________________________slide 11
# differentiating if statements
if (previousExam >= 70):
    print("I passed my first exam with a", previousExam)
if (examGrade >= 70):
    print("I passed my second exam with a", examGrade)
if (newExamGrade >= 70):
    print("I passed my third exam with a ", newExamGrade)

print("My overall exam average is a ", averageExamScore)
# ______________________________________________________________________slide 12
# code blocks and indentation
# emphasize that indentations and colons are important

# print("_"*100)

# Boolean logic
#   1 is True
#   0 is False

# a = 1 
# b = 0 

# print()

# print("a == b", a==b) # 
# print("a < b", a<b)
# print("a > b", a>b)
# print("a != b", a!=b)
# print("a <= b", a<=b)
# print("a >= b", a>=b)

# if a==b:
#     print("a == b", a==b)

# if a<b:
#     print("a < b", a<b)

# if a>b:
#     print("a > b", a>b)

# print("_"*40)

# if a!=b:
#     print("a != b", a!=b)

# if a<=b:
#     print("a <= b", a<=b)

# if a>=b:
#     print("a >= b", a>=b)

# print("_"*40)

