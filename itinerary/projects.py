"""
Project class definition:
project is labelled by name
items are represented with *args which is initialized as an empty list
for each *arg, the empty list is appended to allow for unknown number of items at initialization
project list items can be added, removed, or replaced.
testing calls are blocked out at the end of script.
TO-DO
create overall menu
user input control function
"""
import getpass

class ProjectItem(object):
    def __init__(self, task, due_date=None, complete=False, *contacts):
        self.task = task
        self.due_date = due_date
        self.contacts = contacts
        self.complete = complete

    # if task has extra atributes (is complete, due date, contacts)
    # then these atributes are printed
    def __str__(self):
        if self.complete == True:
            print "    *COMPLETE*"
            # print self.task
        else:
            # print self.task
            if self.due_date != None and self.due_date != False:
                print "    Due: %s" % self.due_date
            if self.contacts != None:
                for name in self.contacts:
                    print "    > %s" % name
                # print "     %s" % name.contact_name
            else:
                pass

    # method relocated to project class
    # incorporated into end of ProjectList instance initialization
    """
    def add_to_item(self, project_menu_instance, task, due_date, complete, *contacts):
        add_on = int(raw_input("would you like to: "
                           "(1) assign a due date? "
                           "(2) attach a contact to this task?"
                           "(3) enter task as-is "))
        if add_on == 1:
            due_date = raw_input("when is this task due?")
            # create event with title "project: task 'due'"
            print "%s is due %s" % (task, due_date)
            self.add_to_item(self, task, due_date, complete, *contacts)
        if add_on == 2:
            # print names of contacts
            contact = raw_input("which contact would you like to attach? ")
            # if item in list, print "contact attached to task"
            # self.contacts.append(contact)
            self.add_to_item(self, task, due_date, complete, *contacts)
        if add_on == 3:
            new_task = ProjectItem(task, due_date, complete, *contacts)
            print "OK"
            new_task.__str__()

        else:
            print "improper selection. try again."
            add_to_item(self, task, due_date, complete, *contacts)
    """

    # function to mark a task as complete
    # to be called in a task edit menu
    def task_complete(self):
        self.complete = True
        print self.task
        self.__str__()
        # send back to project menu somehow.
        # maybe relocate entire function to project class

    # maybe all functions should be in project class
        # aside from init and str




# defines Project class as a name and an unknown number of item arguments
# consider creating new class for project items with attributes such as:
#               due date(tied to calendar), done(true/false), priority?
class Project(object):

    def __init__(self, project_name, *args):
        self.project_name = project_name
        self.args = []
        self.project = {project_name: self.args}
        for arg in args:
            self.args.append(arg)

    # prints project name with complete project list
    # prints each item on the project list with a number system
    # numbers are one higher than list item's index position to account for project name
    def __str__(self):
        x = 1
        print self.project_name
        if len(self.args) > 0:
            for items in self.args:
                print "%s. %s" %(x, items.task)
                items.__str__()
                x += 1
        else:
            print "empty"
    """
    # adds new list items by appending self.args list
    # to do:
    # combine add-item with view items so "if" string is blank, return to menu
    #   if string not blank, add to list
    # even better: create GUI for full list manipulation functionality
    def add_item(self):
        self.__str__()
        new_item = raw_input("Enter item to add: ")
        self.args.append(new_item)"""

    def add_item(self):
        task = raw_input("enter task: ")
        due_date = None
        complete = False
        contacts = []
        # task = ProjectItem(task, due_date, complete, *contacts)
        # self.args.append(task)
        # project_menu_instance = self
        # task.add_to_item(self, project_menu_instance, task, due_date, complete, *contacts)
        add_on = int(raw_input("would you like to: "
                           "(1) assign a due date? "
                           "(2) attach a contact to this task?"
                           "(3) enter task as-is "))
        if add_on == 1:
            task.due_date = raw_input("when is this task due?")
            # create event with title "project: task 'due'"
            print "%s is due %s" % (task, due_date)
            # (self, task, due_date, complete, *contacts)

        if add_on == 2:
            # print names of contacts
            new_contact = raw_input("which contact would you like to attach? ")
            contacts.append(new_contact)
            new_task = ProjectItem(task, due_date, complete, *contacts)
            self.args.append(new_task)
            self.project_menu()
            # if item in list, print "contact attached to task"
            # self.contacts.append(contact)
            # self.add_to_item(self, task, due_date, complete, *contacts)
        if add_on == 3:
            new_task = ProjectItem(task, due_date, complete, *contacts)
            print "OK"
            new_task.__str__()
            self.args.append(new_task)
            self.project_menu()
        #else:
         #   print "improper selection. try again."
         #   add_to_item(self, task, due_date, complete, *contacts)

    # deletes list item
    def delete_item(self):
        self.__str__()
        to_delete = int(raw_input("Which item would you like to delete? "))
        del self.args[to_delete - 1]

    # user can select list item and replace it with new text
    def edit_item(self):
        self.__str__()
        to_edit = int(raw_input("Which item would you like to edit? "))
        self.args[to_edit - 1].__str__()
        print "1. edit task text\n" \
              "2. edit task due-date\n" \
              "3. mark task as complete\n" \
              "4. add or remove a contact\n" \
              "5. return to project"
        item_edit = int(raw_input("make selection: "))
        if item_edit == 1:
            edited_item = raw_input("Enter edited item: ")
            self.args[to_edit - 1].task = edited_item
        if item_edit == 2:
            new_due = raw_input("When is this task due? ")
            self.args[to_edit - 1].due_date = new_due
        if item_edit == 3:
            self.args[to_edit - 1].task_complete()
        if item_edit == 4:
            print "1. add contact \n2. remove contact\n3. cancel"
            contact_to_do = int(raw_input("enter 1, 2 or 3: "))
            if contact_to_do == 1:
                new_contact = raw_input("Which contact to add? ")
                self.args[to_edit - 1].contacts.append(new_contact)
            if contact_to_do == 2:
                for name in self.args[to_edit - 1]:
                    print self.args[to_edit - 1].contacts[name]
                remove_contact = raw_input("Remove which contact?")
                self.args[to_edit - 1].remove(remove_contact)
            if contact_to_do == 3:
                self.edit_item()
        if item_edit == 5:
            self.project_menu()

    # menu function for single project list
    # option 5 needs update
    def project_menu(self, *args):
        project_menu_choice = 0
        print "what would you like to do with this project?"
        print "1. add an item"
        print "2. edit an item"
        print "3. remove an item"
        print "4. view your list"
        print "5. return to project list"
        project_menu_choice = int(raw_input("... "))
        if project_menu_choice == 1:
            self.add_item()
        if project_menu_choice == 2:
            self.edit_item()
        if project_menu_choice == 3:
            self.delete_item()
        if project_menu_choice == 4:
            self.__str__()
            menu = raw_input("press enter to continue")
            self.project_menu()
        # if 5 return to projectlist menu
        # currently returns to display list
        if project_menu_choice == 5:

        if project_menu_choice in range(0, 6) is False:
            print "you made an improper selection"
            self.project_menu()


# class contains list of Project instances
# methods to create new Project, delete whole Project, enter Project-menu

class ProjectList(object):

    def __init__(self, username, *args):
        self.username = username
        self.args = []
        for item in args:
            self.args.append(item)

    # prints the name of all project lists (keys)
    def __str__(self):
        for list in self.args:
            print list.project_name

    # prints list of projects
    # prompts user to select project to inspect
    # sends user to project-specific menu
    def go_to_list(self):
        self.__str__()
        list_choice = raw_input("which list would you like to use?" )
        for list in self.args:
            if list.project_name == list_choice:
                # print "ok"
                list.project_menu(self)
            else:
                pass
        else:
            print "No such list. Try again..."
            self.go_to_list()
# todo      pass username, then projectslist name, then project name
# todo                           down menu chain to allow fro return
    # removes an entire project from project list
    # uses search function and remove() function to remove item
    def delete_list(self):
        self.__str__()
        list_choice = raw_input("which list would you like to erase?" )
        for project in self.args:
            if project.project_name == list_choice:
            #    print "ok"
                # need to remove list
                self.args.remove(list)
            #    list.project_name.__str__()
                self.__str__()

    # this function creates Project class instance (single to-do list)
    # after instance initialization, user enters project-menu
    def create_list(self):
        project_name = raw_input("What would you like to name your new project? ")
        # new_list = Project(str(new_list))
        # new_list.project_menu(self)
        project_name = Project(project_name)
        self.args.append(project_name)
        project_name.project_menu()

    def project_list_menu(self):
        print "1. new project"
        print "2. view projects"
        print "3. select a project"
        choice = raw_input("make a selection: ")
        if int(choice) == 1:
            self.create_list()
        if int(choice) == 2:
            self.__str__()
        if int(choice) == 3:
            self.go_to_list()


# update formatting of Project instance to be created
# match with delete function
#    def create_list(self):
#        project_name = raw_input("What is the name of your project? ")
#        project_name = Project(project_name)
#        project_name.__str__()

# user class has username and password pair to be checked at login
# will contain methods to access different functionalities
# should create empty instances for child classes (ProjectList, Calendar, etc)
# should house user-menu to send to sub-functionality-specific menus
class User(object):
    def __init__(self, username, password, projects):
        self.username = username
        self.password = password
        self.projects = projects
        # self.create_project_list(username)

    # main menu for individual user
    def user_menu(self):
        print "1. projects\n" \
              "2. calendar\n" \
              "3. contacts"
        choice = raw_input("selection: ")
        if int(choice) == 1:
            self.projects.project_list_menu()


class UserList(object):
    def __init__(self, *args):
        self.args = []
        for item in args:
            self.args.append(item)

    # THIS FUNCTION PRINTS USERNAME AND PASSWORD
    # IT IS ONLY FOR TESTING, SHOULD BE HASHED OUT AND REMOVED FROM PROTOCOL
    def __str__(self):
        for user in self.args:
            print user.username
            print user.password
            #print user.projects.project_name

    # FUNCTION CHECKS FOR MATCHED USERNAME AND PASSWORD PAIR
    # IF MATCHED, SEND USER TO USER-SPECIFIC MENU
    # user.create_project_list() is a testing stand-in
    def log_in(self):
        self.__str__()
        user_login = raw_input("enter username: ")
        for user in self.args:
            if user.username == user_login:
                print "ok"
                password = getpass.getpass("enter password: ")
                if password == user.password:
                    user.user_menu()
            else:
                pass

    # CREATES NEW INSTANCE OF USER CLASS
    # STORES USERNAME AND PASSWORD FOR CHECKING LATER
    def new_user(self):
        username = raw_input("new username: ")
        for user in self.args:
            if username == user.username:
                print "there is already an account with that name."
                self.new_user()
            else:
                pass
        password = getpass.getpass("new password: ")
        confirm_password = getpass.getpass("confirm password: ")
        while password != confirm_password:
            print "re-enter your password, there was a problem with confirmation"
            self.new_user()
            password = getpass.getpass("new password: ")
            confirm_password = getpass.getpass("confirm password: ")

        else:
            projects = ProjectList(username)
            # contacts = ContactBook(username)
            # appointments = AppontmentBook(username)
            username = User(username, password, projects)
            self.args.append(username)
            self.__str__()
            print "New user account created."
            print "please login"
            self.start_menu()

    # TOP LOGIN MENU
    #SENDS USER TO LOGIN OR CREATE USER FUNCTION
    def start_menu(self):
        print "1. login"
        print "2. new user"
        start_menu_choice = raw_input("enter selection: ")
        if int(start_menu_choice) == 1:
            self.log_in()
        if int(start_menu_choice):
            self.new_user()
        else:
            print "improper selection."
            print "try again"
            self.start_menu()

one = ProjectItem("one", complete = True)
two = ProjectItem("two")
three = ProjectItem("three")
#projects1 = ProjectList(alex)
#projects2 = ProjectList(test)
test_project = Project("test", one, two, three)
test_list = Project("list", "first", "second", "third")

TEST = ProjectList(test_project, test_list)
#alex = User(username="alex", password="pw123", projects=ProjectList(alex))
#test = User(username="test", password="test", projects=ProjectList(test))
main = UserList()
# test_project.project_menu()
# one.task_complete()
# alex.create_project_list()
main.start_menu()
# TEST.create_list()
# TEST.create_list()
#TEST.__str__()
# print TEST
#TEST.__str__()


#test_project.__str__()
#test_project.add_item()
#test_project.__str__()
#test_project.delete_item()
#test_project.__str__()
#test_project.edit_item()
#test_project.__str__()
#test_project.project_menu()

