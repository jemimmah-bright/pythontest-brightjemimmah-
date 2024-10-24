# Question (2)
# Write a Python program to ask a student to enter their mark scored and it returns
# the grade obtained according to the following:
# Percentage >= 90%: Grade A
# Percentage >= 80%: Grade B
# Percentage >= 70%: Grade C
# Percentage >= 60%: Grade D
# Percentage >= 40%: Grade E
# Percentage < 40%:  Grade F
def marks_scored ():
 marks_scored = int (input ("Enter your scored marks in    :"))
 if marks_scored >= 90 :
  print ("grade A")
 elif marks_scored >= 80 :
  print ("grade B")
 elif marks_scored >= 70 :
  print ("garde C")
 elif marks_scored >= 60 :
  print ("garde D")
 elif marks_scored >= 40 :
  print ("garde E")
 else :
  print ("grade F")
marks_scored ()

