#simple grading system for python class (python for teachers)

#create the table
def table(data):

	#calculate the maximum length	
	col_width = max(len(word) for row in data for word in row) + 2  # padding
	for row in data:
		#do the padding
	    print ("".join(word.ljust(col_width) for word in row))

#calculate the average score of a student
def average(data):
	#list to keep all the average marks
	list_of_scores = []

	#to aid in printing
	student_number = 1

	#iterate through each of the student's data
	for student in data:
		#initialize the total score to 0 for every student
		total = 0
		#iterate through the scores in each of student's data
		for subject in student : 
			#add the score into the variable
			total += int(subject)

		average_score = total/len(student) #calculate the average
		print("The average mark of student "+ str(student_number) + " is : ", average_score) #print out the scores
		list_of_scores.append(average_score) #append in the list
		student_number += 1 #increment

	return list_of_scores

#calculate the highest mark
def highest(data):

	highest_value = max(data)
	return data.index(highest_value) + 1


#exception handling to avoid anything other than integers to be inputted
try:
	#get the inputs from the users
	number_of_student = int(input("Please input the number of student(s) : "))
	number_of_subject = int(input("Please input the number of subject(s) : ")) 

	#create a 2-dimensional array
	matrix = [[0 for i in range(number_of_subject)] for j in range(number_of_student)]
	
	#loop through the number of students
	for x in range(number_of_student):
		#loop through the number of subjects
		for z in range(number_of_subject):

			subject_score = str(input("Please input the score of subject " + str(z + 1) + " of student " + str(x+1) + " : "))
			matrix[x][z] = subject_score
	#function call
	table(matrix) #print the table
	average_marks = average(matrix) #get the average marks of the student
	highest_rank_student = highest(average_marks) #get the student with the highest average score
	print("The student with the highest score is Student " , highest_rank_student) #print out the highest scorer

#error handling code
except Exception as e:
	#print the error
	print("Error : ", e)




