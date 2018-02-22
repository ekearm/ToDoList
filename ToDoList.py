import sys

def option1():
	finished = " "
	with open("ToDoList.txt") as textFile:
		textFile.seek(0)
		firstCharacter = textFile.read(1)
		textFile = open("ToDoList.txt", "w")
		if not firstCharacter:
			print"The file is empty"
			textFile.write(raw_input("Enter your item followed by Enter: \n"))
			finished = raw_input("Enter Done and hit Return when finished: ")
			if (finished == "Done" or finished == "done" or finished == "DONE"):
				print "\n"
			else:

				while (finished != "done" or finished != "Done" or finished != "DONE"):
					textFile.write("\n")
					textFile.write(raw_input("Enter your item followed by Enter: \n"))
					finished = raw_input("Enter Done and hit Return when finished: ")
					if (finished == "Done" or finished == "done" or finished == "DONE"):
						break
		else:
			print "The file is not empty adding to the last line"
			while True:
				textFile  = open("ToDoList.txt", "r")
				line = textFile.readline()
				if line == '' :
					textFile = open("ToDoList.txt", "a")
					textFile.write("\n")
					textFile.write(raw_input("Enter your item followed by Enter: \n"))
					finished = raw_input("Enter Done and hit Return when finished: ")
					if (finished == "Done" or finished == "done" or finished == "DONE"):
						print "\n"
					else:

						while (finished != "done" or finished != "Done" or finished != "DONE"):
							textFile.write("\n")
							textFile.write(raw_input("Enter your item followed by Enter: \n"))
							finished = raw_input("Enter Done and hit Return when finished: ")
							if (finished == "Done" or finished == "done" or finished == "DONE"):
								break
					break
	textFile.close()

def option2():
	textFile = open("ToDoList.txt", "r")
	print textFile.read()

	textFile.close()

def option3():
	textFile = open("ToDoList.txt", "w")
	textFile.truncate()

	textFile.close()

def main():
	option = 0
	while (option != 1 or option != 2 or option != 3 or option != 4):
		print "1. Enter an item"
		print "2. Veiw To Do List"
		print "3. Erase an item"
		print "4. Exit"
		option = int(raw_input("Please make your selection: "))

		if (option == 1):
			option1()
		elif (option == 2):
			option2()
		elif (option == 3):
			option3()
		elif(option == 4):
			print("Thank you! Come again!")
			quit()
		else:
			print("Enter a valid selection. Please")

main()