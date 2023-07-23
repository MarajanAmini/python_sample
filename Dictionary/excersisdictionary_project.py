students= dict()
def add():
	number = input("student's number :")
	if number not in students.keys():
		f_name= input("first name  :")
		l_name = input(" last name :")
		class_number = input(" class number:")
		math_score = float(input(" math score :"))
		English_score = float(input("english score :"))
		python_score = float(input("python score :"))
		student = {}
		student.update({"first name":f_name,
			"last name":l_name,
			"class_number":class_number,
			"math_score":math_score,
			"English_score":English_score,
			"python_score":python_score})
		students[number]=student
	else:
		print("already exist!")
def edit(number):
	if number in students.keys():
		students[number]["first name"]= input("a new f_name :")or students[number]["first name"]
		students[number]["last name"]=input("a new l_name :")or students[number]["last name"]
		students[number]["class_number"]=input("new class number:")or students[number]["class_number"]
		students[number]["math_score"] =input("a new math_score:")or students[number]["math_score"]
		students[number]["English_score"]=input("A new English_score:")or students[number]["English_score"]
		students[number]["python_score"]=input("a new python_score")or students[number]["python_score"]

	else:
		print("not found student's number!")

def search(number):
	if number in students.keys():
		for i in students[number]:
			print(f"{i}---->{students[number][i]}")
	else:
		print("not found the number")
def remove(number):
	if number in students.keys():
		students.pop(number)
		print("removed")
	else:
		print("not found number!")

def details(name_corse):
	list_scores = []
	for i in students :
		score = students[i][name_corse]
		list_scores.append(score)
	min_score = min(list_scores)
	max_score = max(list_scores)
	l_score = len(list_scores)
	sum_score = sum(list_scores)
	avg_score = sum_score / l_score
	return min_score,max_score,avg_score







while True:
	answer = input("select an option :")
	if answer == "add":
		add()
	elif answer == "edit":
		number = input("a new number of student :")
		edit(number)

		
	elif answer == "search":
		number=input("a number of student")
		search(number)
	elif answer == "remove":
		number = input(" a number of student:")
		remove(number)
	elif answer == "display":
		display()
	elif answer == "details":

		min_math,max_math,avg_math = details("math_score")
		min_english,max_english,avg_english = details("English_score")
		min_python,max_python,avg_python = details("python_score")

		print(f"math ---> min:{min_math},max:{max_math},avg:{avg_math}")
		print(f"english---> min:{min_english},max:{max_english},avg:{avg_english}")
		print(f"python ---> min:{min_python},max:{max_python},avg:{avg_python}")


	elif answer == "exit":
		break
	elif answer == "":
		pass
	else:
		print(f"{answer}:command not found !")

