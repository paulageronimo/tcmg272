integer = 0
string = "zero"
floating = 0.0
#boolean = False # 0 - false ; 1 is true

# type()

#print("integer", integer, "is a ", type(integer))
#print("string", string, "is a ", type(string))
#print("floating", floating, "is a ", type(floating))
#print("boolean", boolean, "is a ", type(boolean))

print("_______")
examGrade = 74

perfectScore = (examGrade == 100)
print("I have a perfect score.", perfectScore)

negative = (examGrade < 0)
print("I have a negative grade.", negative)
genius = (examGrade > 100)
print("I am a genius.", genius)
failing = (examGrade <= 69)
print("I am failing.", failing)
passing = (examGrade >= 70)
print("I am passing.", passing)
# == <= >=
#print("2" < 3)

print("Tuesday" == "tuesday")
print("_______")
previousExam = 95
passedPreviousExam = True

passedAllExams = (passing and passedPreviousExam)
# and
print("I have passed all my exams.", passedAllExams)
# or 
haveGrade = passing or failing
print("I have a grade for my exam.", haveGrade)
# not
positiveGrade = not negative 
print("I have a positive/valid grade.", positiveGrade)

notSimilarGrade = (previousExam != examGrade)
print("I do not have similar grades for both exams.", notSimilarGrade)
print("_______")
newExamGrade = 66

if (newExamGrade >= 70):
    print("I passed my exam.")
else:
    print("I failed my exam.")
    print("_______")
if (newExamGrade >= 90):
    print("A")
elif (newExamGrade >=80):
    print("B")
elif (newExamGrade >= 70):
    print("C")
elif (newExamGrade >= 60):
    print("D")
else:
    print("F")
print("_______")
average = (previousExam + examGrade + newExamGrade) / 3

print(average)

print("_______")

if (average >= 70):
    if (average > 100):
        print("I passed and I am a genius.")
    else:
        print("I passed.")
else:
    print("I failed.")
if (average >= 70):
        if (average > 100):
            print("I am a genius.")
        print("I passed.")
else:
        print("I failed.")

