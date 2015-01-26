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




"""
test_project = Project("test", 'one', "two", "three")
test_project.__str__()
test_project.add_item()
test_project.__str__()
test_project.delete_item()
test_project.__str__()
test_project.edit_item()
test_project.__str__()
"""