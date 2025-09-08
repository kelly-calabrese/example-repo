# ===== Importing external modules =====

import os
current_dir = os.path.dirname(__file__)
file_path_users = os.path.join(current_dir, 'user.txt')
file_path_tasks = os.path.join(current_dir, "tasks.txt")
file_path_task_overview = os.path.join(current_dir, "task_overview.txt")
file_path_user_overview = os.path.join(current_dir, "user_overview.txt")

from datetime import date, datetime
date_format = "%d %b %Y"
today = date.today()

# === Class Creation ===


class Task:
    def __init__(self, username, title, description, assign_date,
                 due_date, status):
        self.username = username
        self.title = title
        self.description = description
        self.assign_date = assign_date
        self.due_date = due_date
        self.status = status
        '''
        In this function, the following attributes are initiated:
            ● username of person with task assigned,
            ● task title,
            ● task description,
            ● assignment date
            ● due date, and
            ● completion status.
        '''
    def __str__(self):
        return f"{self.username}, {self.title}, {self.description}, {self.assign_date}, {self.due_date}, {self.status}\n"


class LogIn:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f"{self.username}, {self.password}\n"


# === Task and Users List ===

task_list = []
users_list = []

# === Functions Outside Class ===


def read_tasks(file_path_tasks):
    try:
        with open(file_path_tasks, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip('\n').split(", ")
                new_task = Task(line[0], line[1], line[2],
                                line[3], line[4], line[5])
                task_list.append(new_task)
    except ImportError:
        print("\nError. File not found.\n")
    '''
    This function reads the task file and maps them to a Task class object.
    '''


def view_all(task_list):
    task_number = 0
    for self in task_list:
        task_number = task_number + 1
        print("________________________________________________\n"
              f"Task #{task_number}\n"
              f"Task:              {self.title}\n"
              f"Assigned to:       {self.username}\n"
              f"Date assigned:     {self.assign_date}\n"
              f"Due date:          {self.due_date}\n"
              f"Task complete?     {self.status}\n"
              f"Task description:  \n{self.description}\n"
              "________________________________________________\n")
    '''
    This function prints the Task objects collected as a table.
    '''


def update_task_file(task_list):
    try:
        with open(file_path_tasks, "w") as file:
            for tasks in task_list:
                file.write(str(tasks))
    except ImportError:
        print("\nError. Return to menu.\n")

    ''' This function writes the task list to a text file.'''


def read_users(file_path_users):
    try:
        with open(file_path_users, "r+") as file:
            lines = file.readlines()
            for line in lines:
                line = line.rstrip('\n').split(", ")
                new_user = LogIn(line[0], line[1])
                users_list.append(new_user)
    except ImportError:
        print("\nError. File not found.\n")
    '''
    This function reads the users file and maps them to a LogIn class object.
    '''


def view_mine(user_input, task_list):
    user_found = False
    task_number = 0
    for self in task_list:
        task_number = task_number + 1
        if self.username == user_input:
            print("________________________________________________\n"
                  f"Task #{task_number}\n"
                  f"Task:              {self.title}\n"
                  f"Assigned to:       {self.username}\n"
                  f"Date assigned:     {self.assign_date}\n"
                  f"Due date:          {self.due_date}\n"
                  f"Task complete?     {self.status}\n"
                  f"Task description:  \n{self.description}\n"
                  "________________________________________________\n")
            user_found = True
    if user_found is False:
        print("\nNo tasks found.\n")

    task_status_update = input("\nEnter a task number to update task "
                               "or \"-1\" to return to menu: ")
    try:
        task_status_update = int(task_status_update)
    except ValueError:
        task_status_update = input("\nInvalid input.\n"
                                   "Enter a task number to update task "
                                   "or \"-1\" to return to menu: ")
    while True:
        if task_status_update != -1:
            edit_task(task_list, task_status_update)
            break
        elif task_status_update == -1:
            break
        else:
            task_status_update = input("\nInvalid input.\n"
                                       "Enter a task number to update task "
                                       "or \"-1\" to return to menu: ")

    '''
    This function prints the Task objects assigned to a specific user.
    '''


def reg_user(users_list):
    username = input("Enter the username for the new user:\n").lower()
    user_exists = 0

    while True:
        for user in users_list:
            if user.username == username:
                user_exists += 1
        if user_exists > 0:
            username = input("Invalid input. User already exists.\n"
                             "Enter new username: ").lower()
        else:
            break

    password = input("Create a password for the new user:\n")
    new_user = LogIn(username, password)
    users_list.append(new_user)
    confirmation = input("\nRe-enter password for confirmation: ")

    while True:
        if confirmation == password:
            try:
                with open(file_path_users, "w") as file:
                    for users in users_list:
                        file.write(f"{users}")
            except ImportError:
                print("\nImport Error. Return to menu.\n")
            print("\nUser password confirmed.\n")
            print(f"New user registered.\n\
                    Username: {username}\n\
                    Password: {password}\n")
        else:
            confirmation_choice = input("\nPassword does not match."
                                        "\nEnter \"Y\" to retry or "
                                        "\"N\" to return to menu: ")
            confirmation_choice = confirmation_choice.upper()
            if confirmation_choice == "Y":
                confirmation = input("\nPlease re-enter password "
                                     "for confirmation: ")
        break

    '''
    This function adds a user and password to the user list
    as a LogIn class object. Then prints the new user information.
    '''


def login_password(user_input, users_list, found_password):
    password_input = input("Enter password:\n")
    while True:
        for users in users_list:
            if user_input == users.username:
                correct_password = users.password

        if password_input == correct_password:
            print("Login successful.\n\n")
            found_password = True

        if found_password is False:
            password_input = input("Invalid password.\n"
                                   "Please try again."
                                   "\n\nEnter password: ")
        else:
            break
    '''
    This function checks a user inputted password agains the password
    that corresponds to the username given. The user is prompted for
    a valid password until one is given.
    '''


def view_completed(task_file):
    completed_found = False
    task_number = 0
    for self in task_file:
        task_number = task_number + 1
        if self.status == "Yes":
            completed_found = True
            print("________________________________________________\n"
                  f"Task #{task_number}\n"
                  f"Task:              {self.title}\n"
                  f"Assigned to:       {self.username}\n"
                  f"Date assigned:     {self.assign_date}\n"
                  f"Due date:          {self.due_date}\n"
                  f"Task complete?     {self.status}\n"
                  f"Task description:  \n{self.description}\n"
                  "________________________________________________\n")
    if completed_found is False:
        print("\nNo completed projects found.\n\n")
    ''' This function displays all tasks marked complete.'''


def edit_task(task_list, task_status_update):
    task_found = False
    task_number = 0

    def edit_choice_1():
        self.username = input("\nUsername to be assigned:\n").lower()

    def edit_choice_2():
        self.due_date = input("\nDue date to be assigned in "
                              "format \"DD Mmm YYYY\":\n")
        while True:
            try:
                datetime.strptime(self.due_date, date_format).date()
                break
            except ValueError:
                self.due_date = input("\nIncorrect date format.\n"
                                      "Please use format \"DD Mmm YYYY\":\n")

    for self in task_list:
        task_number = task_number + 1
        if task_number == task_status_update:
            update_choice = input("Enter \"Status\" to update status "
                                  "or \"Edit\" to update user "
                                  "assignment or due date: ")
            update_choice = update_choice.lower()
            if update_choice == "status":
                self.status = "Yes"
                print("\nStatus changed to complete.\n\n")
            elif update_choice == "edit":
                if self.status == "Yes":
                    print("Cannot change completed tasks.")
                else:
                    while True:
                        edit_choice = input("Type number for editing choice:\n"
                                            "1 - Change username\n"
                                            "2 - Change due date\n"
                                            "3 - Change both username "
                                            "and due date\n"
                                            "Number: ")
                        if edit_choice == "1" or edit_choice == "3":
                            edit_choice_1()
                            break
                        elif edit_choice == "2" or edit_choice == "3":
                            edit_choice_2()
                            break
                        else:
                            edit_choice = input("\nInvalid input.\n"
                                                "Type number for editing "
                                                "choice:\n"
                                                "1 - Change username\n"
                                                "2 - Change due date\n"
                                                "3 - Change both username "
                                                "and due date\n"
                                                "Number: ")
            else:
                update_choice = input("\nInvalid input.\n"
                                      "Enter \"Status\" or \"Edit\" "
                                      "to update: ")
            task_found = True

    if task_found is False:
        print("\nTask not found.\n\n")
    '''This function changes the status of a task from No to
    Yes to mark it complete.'''


def delete_task(task_list):
    task_found = False
    task_delete = input("\nEnter the task number to be deleted:"
                        "\n")
    try:
        task_delete = int(task_delete)
    except ValueError:
        task_delete = input("\nTask number needs to be an integer.\n"
                            "Please enter the task number to delete: ")
    task_number = 0
    edit_list = []
    for tasks in task_list:
        task_number = task_number + 1
        if task_delete == task_number:
            task_found = True
        else:
            edit_list.append(tasks)
            update_task_file(edit_list)
    if task_found is False:
        print("\nTask not found.\n\n")
    return edit_list

    ''' This function rebuilds the task list without the task to be deleted'''


def add_task():
    title = input("\nEnter a title for the new task:\n")
    description = input("\nEnter a description for this task:\n")
    username = input("\nEnter the username of the person "
                     "assigned to the task:\n")
    username = username.lower()
    assign_date = today.strftime(date_format)
    assign_date = str(assign_date)
    due_date = input("\nEnter the task due date in format "
                     "\"DD Mmm YYYY\":\n")
    while True:
        try:
            datetime.strptime(due_date, date_format).date()
            break
        except ValueError:
            due_date = input("\nIncorrect date format. Please use format "
                             "\"DD Mmm YYYY\":\n")
    status = 'No'
    new_task = Task(username, title, description, assign_date,
                    due_date, status)
    task_list.append(new_task)
    update_task_file(task_list)
    print("\n\nTask assigned with today's date.\n"
          "Completion status is set to 'No' by default.\n")
    ''' This function writes a new Task object based on user input.'''


def generate_reports(task_list, users_list):

    # Task Overview

    task_count = 0
    completed_count = 0
    incomplete_count = 0
    over_due_count = 0

    for tasks in task_list:
        task_count += 1
        if tasks.status == "Yes":
            completed_count += 1
        else:
            incomplete_count += 1
            if datetime.strptime(tasks.due_date, date_format).date() < today:
                over_due_count += 1

    total_tasks = task_count
    total_completed = completed_count
    total_uncompleted = incomplete_count
    total_overdue = over_due_count

    if total_tasks == 0:
        print("No tasks found.\n")
        pct_incomplete = "NA"
    else:
        pct_incomplete = round((incomplete_count/total_tasks)*100, 1)

    if total_uncompleted == 0:
        print("No incomplete tasks found.\n")
        pct_overdue = "NA"
    else:
        pct_overdue = round((total_overdue/total_uncompleted)*100, 1)

    try:
        with open(file_path_task_overview, "w") as file:
            file.write(f"___________________________________________________"
                       "\n"
                       f"OVERALL TASK SUMMARY\n"
                       f"   Total number of tasks in manager: {total_tasks}\n"
                       f"   Number of completed tasks: "
                       f"{total_completed}\n"
                       f"   Number of uncompleted tasks: "
                       f"{total_uncompleted}\n"
                       f"   Number of overdue and incomplete tasks: "
                       f"{total_overdue}\n"
                       f"   Percent of tasks incomplete: "
                       f"{pct_incomplete} %\n"
                       f"   Percent of incomplete tasks that are overdue: "
                       f"{pct_overdue} %\n"
                       f"____________________________________________________"
                       "\n\n")
    except ImportError:
        print("\nError. Return to menu.\n")

    # User Overview
    # Overall User Summary

    user_count = 0
    all_usernames = []
    for users in users_list:
        user_count += 1
        all_usernames.append(users.username)

    total_users = user_count
    unique_usernames = list(set(all_usernames))

    try:
        with open(file_path_user_overview, "w") as file:
            file.write(f"\nOVERALL USER SUMMARY\n\n"
                       f"Total number of users: {total_users}"
                       f"\nTotal number of tasks in manager: {total_tasks}\n"
                       f"\n\n")
    except ImportError:
        print("\nError. Return to menu.\n")

    # Summary By User

    for name in unique_usernames:
        user_task_number = 0
        completed_count = 0
        over_due_count = 0
        incomplete_count = 0
        for tasks in task_list:
            if name == tasks.username:
                user_task_number += 1
                if tasks.status == "Yes":
                    completed_count += 1
                elif tasks.status == "No":
                    incomplete_count += 1
                    if datetime.strptime(tasks.due_date, date_format).date() < today:
                        over_due_count += 1
        if user_task_number == 0:
            print(f"\nNo tasks found for user {name}.\n")
            pct_user_tasks = "NA"
            pct_completed = "NA"
            pct_noncompleted = "NA"
        else:
            pct_user_tasks = round(100*(user_task_number/total_tasks), 1)
            pct_completed = round(100*(completed_count/user_task_number), 1)
            pct_noncompleted = 100 - pct_completed

        if incomplete_count == 0 or user_task_number == 0:
            print(f"\nNo incomplete tasks found for user {name}.\n")
            pct_overdue = "NA"
        else:
            pct_overdue = round(100*(over_due_count/incomplete_count), 1)

        try:
            with open(file_path_user_overview, "a") as file:
                file.write(f"Username: {name}\n"
                           "  Total number of tasks assigned: "
                           f"{user_task_number}\n"
                           "  Percent of total tasks assigned to current user:"
                           f" {pct_user_tasks} %\n"
                           "  Percent of assigned tasks completed: "
                           f"{pct_completed} %\n"
                           "  Percent of tasks to be completed: "
                           f"{pct_noncompleted} %\n"
                           "  Percent of incomplete tasks that are overdue: "
                           f"{pct_overdue} %\n\n")
        except ImportError:
            print("\nError. Return to menu.\n")

    ''' This function calculates summary statistics overall and per user,
    then writes the results to a text file.'''


def display_statistics(task_list, users_list):
    generate_reports(task_list, users_list)

    with open(file_path_task_overview, "r") as file:
        lines_task = file.read()
        print(lines_task)

    with open(file_path_user_overview, "r") as file:
        lines_user = file.read()
        print(lines_user)

    '''This function prints the report statistics from the text files
    to the terminal after genrating the current reports'''


def switch_user():
    user_input = input("Enter username:\n")
    user_input = user_input.lower()
    found_user = False
    found_password = False

    while True:
        for users in users_list:
            if user_input == users.username:
                print("\nUsername found.\n\n")
                login_password(user_input, users_list, found_password)
                found_user = True
        if found_user is False:
            print("\nUsername not found.\n"
                  "Please enter a valid username to proceed.\n\n")
            user_input = input("Enter username:\n")
            user_input = user_input.lower()
        else:
            break
    if user_input == "admin":
        is_admin = True
    else:
        is_admin = False

    return user_input, is_admin


# ==== Login Section ====


read_users(file_path_users)
read_tasks(file_path_tasks)

user_input = input("Enter username:\n")
user_input = user_input.lower()
found_user = False
found_password = False
is_admin = False

while True:
    for users in users_list:
        if user_input == users.username:
            print("\nUsername found.\n\n")
            login_password(user_input, users_list, found_password)
            found_user = True
    if found_user is False:
        print("\nUsername not found.\n"
              "Please enter a valid username to proceed.\n\n")
        user_input = input("Enter username:\n")
        user_input = user_input.lower()
    else:
        break

if user_input == "admin":
    is_admin = True

# === Menu Section ===


while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    if is_admin is False:
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
su - switch user
e - exit
: ''').lower()
    else:
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete tasks
ds - display statistics
gr - generate reports
su - switch user
e - exit
: ''').lower()
    print(menu)

    if menu == 'r':
        if user_input == "admin":
            reg_user(users_list)
        else:
            print("Access denied. Only the admin can add users.\n\n")

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all(task_list)

    elif menu == 'vm':
        view_mine(user_input, task_list)

    elif menu == 'vc':
        view_completed(task_list)

    elif menu == 'del':
        edit_list = delete_task(task_list)
        task_list = edit_list

    elif menu == 'ds':
        display_statistics(task_list, users_list)

    elif menu == 'gr':
        generate_reports(task_list, users_list)

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    elif menu == 'su':
        user_input, is_admin = switch_user()

    else:
        print("You have entered an invalid input. Please try again")
