#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

#====functions ====================

def reg_user():

#Enter the new username and conformation password and as the process is so short I decided not to put it in a loop      
        if username_input == "admin":
            unique = False
            while unique == False:

                new_user = input("Please enter the new user name: ")

                if new_user == "-1":
                    return

                with open('user.txt', 'r') as user_file:
                    for current_line in user_file.readlines():
                        current_line = current_line.replace("\n", "")

                        x = current_line.split(", ")
# add the username to the username list 
                        user_list.append(x[0])

#checks if user is unique and if it it isn't it stops the registration process            
                    for i in range(0, len(user_list)):
                        if new_user == user_list[i]:
                            print("This user already exists please enter a unique username \n")
                            unique = False
                            break                      
                        elif new_user != user_list[i]:
                            unique = True

            new_pass = input("Please enter the new password: ")
            conf_pass = input("please confirm your password: ")

            if new_pass == conf_pass:
# Only writes to the user.txt file if the passwords match
                with open('user.txt', 'a') as user_file:
# Put the \n at the start of the statement so that it works with the legacy accounts otherwise I would have put it at the end
                    user_file.write("\n" + new_user + ", " + new_pass)
                
                print("User added \n")
            else:
                print("I'm sorry your passwords don't match please try again.")
        else:
            print("You are not authorized to add a new users")


def add_task():

    task_user = input("Please enter who this task is for: ")
    task_title = input ("Please enter the title of the task: ")
    task_description = input("Please enter a description of the task: ")
#gets todays date       
    today = date.today()
#converts todays date into the required format
    current_date = today.strftime("%d %b %Y")
#In an ideal world I would find some method to validate this input with something similar to an input mask 
#but this is probably outside the scope of this project
    due_date = input("Please enter when this task is due for completion (DD MMM YYYY): ") 

    with open('tasks.txt', 'a') as task_file:
        task_file.write("\n"+ task_user + ", " + task_title + ", " + task_description + ", " + current_date + ", " + due_date + ", No")

def view_all():
    
    with open('tasks.txt','r') as task_file:
            for current_line in task_file.readlines():
                task_breakdown = current_line.split(", ")
        # Take each element of the split list and assign it to the designated heading 
                print("Task: \t" + task_breakdown[1])
                print("Assigned to: \t" + task_breakdown[0])
                print("Date assigned: \t" + task_breakdown[3])
                print("Date Due: \t" + task_breakdown[4])
                print("Task Complete: \t" + task_breakdown[5])
                print("Task Description: \t" + task_breakdown[2])

def view_mine():

    task_counter = 1
    
    with open('tasks.txt','r') as task_file:
            for current_line in task_file.readlines():
                task_breakdown = current_line.split(", ")
        # using the username_input variable login on the logic that they wouldn't be able to access this part of the 
        # program if it was incorrect
                if task_breakdown[0] == username_input:

                    print(f"Task Number: {task_counter}")
                    print("Task: \t" + task_breakdown[1])
                    print("Assigned to: \t" + task_breakdown[0])
                    print("Date assigned: \t" + task_breakdown[3])
                    print("Date Due: \t" + task_breakdown[4])
                    print("Task Complete: \t" + task_breakdown[5])
                    print("Task Description: \t" + task_breakdown[2] + "\n")

                    task_counter += 1
            
    user_input = int(input("Please select a task number: "))
    task_counter = 1
    with open('tasks.txt','r') as task_file:
        for current_line in task_file.readlines():
            task_breakdown = current_line.split(", ")
           
            if task_breakdown[0] == username_input:

                if user_input == task_counter:

                    print(f"Task Number: \t {task_counter}")
                    print("Task: \t" + task_breakdown[1])
                    print("Assigned to: \t" + task_breakdown[0])
                    print("Date assigned: \t" + task_breakdown[3])
                    print("Date Due: \t" + task_breakdown[4])
                    print("Task Complete: \t" + task_breakdown[5])
                    print("Task Description: \t" + task_breakdown[2] + "\n")
            
                else:
                    task_counter += 1

                
                

def stats():
    print(f"Number of users: \t {len(user_list)}")
        # As the file isn't guaranteed to be pre-read like the user file the system will need to make a run through the file 
        # and count the number of outstanding jobs then print the result
    task_counter = 0
    with open('tasks.txt', 'r') as task_file:
        for current_line in task_file.readlines():
            task_counter += 1
            
    print(f"Number of tasks: \t {task_counter}")


#====Login Section====

#Keeping the username and password separate so if someone finds one they wont have complete access to the system
user_list = []
pass_list = []
user_access = False

#reads in user file and then splits the username and password
with open('user.txt', 'r') as user_file:
    for current_line in user_file.readlines():
        current_line = current_line.replace("\n", "")

        x = current_line.split(", ")
# add the username to the username list and password to the password list
        user_list.append(x[0])
        pass_list.append(x[1])
    user_file.close()

while user_access != True:
    username_input = input("Please enter your username: ")
    password_input = input("Please enter your password: ")
    for i in range(0, len(user_list)):
#Check both the username and password together so that if someone was trying 
# to get into the system illicitly they couldn't find out a username by mistake
        if username_input == user_list[i] and password_input == pass_list[i]:
            user_access = True
            break
    else:
        print("Either the username or password you've entered are incorrect please try again.")
        user_access = False

while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    if username_input != "admin":

        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
    : ''').lower()

    elif username_input == "admin":
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        s - view statistics
        e - Exit
    : ''').lower()


    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task()     
        

    elif menu == 'va':

        view_all()  

    elif menu == 'vm':

        view_mine()  
        
    elif menu == 's':
        # This is to prevent a user from accidentally stumbling onto the information
        if username_input == "admin":
            stats()
        else: 
            print("You have made a wrong choice, Please Try again")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")