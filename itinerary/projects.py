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

# defines Project class as a name and an unknown number of item arguments
class Project(object):
    def __init__(self, project_name, *args):
        self.project_name = project_name
        self.args = []
        for arg in args:
            self.args.append(arg)

# prints project name with complete project list
# prints each item on the project list with a number system
# numbers are one higher than list item's index position to account for project name
    def __str__(self):
        print self.project_name
        x = 1
        for items in self.args:
            print "%s. %s" %(x, items)
            x += 1

# adds new list items by appending self.args list
    def add_item(self):
        self.__str__()
        new_item = raw_input("Enter item to add: ")
        self.args.append(new_item)

# deletes list item
    def delete_item(self):
        self.__str__()
        to_delete = int(raw_input("Which item would you like to delete? "))
        del self.args[to_delete - 1]

# user can select list item and replace it with new text
    def edit_item(self):
        self.__str__()
        to_edit = int(raw_input("Which item would you like to edit? "))
        print self.args[to_edit - 1]
        edited_item = raw_input("Enter edited item: ")
        self.args[to_edit - 1] = edited_item

# menu function for single project list
    def project_menu(self):
        print "what would you like to do with this project?"
        print "1. add an item"
        print "2. edit an item"
        print "3. remove an item"
        print "4. view your list"
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
        else:
            print "you made an improper selection"
            self.project_menu()


"""
class ProjectList(object):

    def __init__(self, *args):
        self.args = {}
        for item in args:
            self.args[item] = item

    def __str__(self):
        for item in self.args:
            print item



test_project = Project("test", 'one', "two", "three")
test_list = Project("list", "first", "second", "third")

test_ProjectList = ProjectList(test_project, test_list)
test_ProjectList.__str__()
#test_project.__str__()
#test_project.add_item()
#test_project.__str__()
#test_project.delete_item()
#test_project.__str__()
#test_project.edit_item()
#test_project.__str__()
#test_project.project_menu()

"""