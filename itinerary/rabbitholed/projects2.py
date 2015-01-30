class Task(object):
    def __init__(self, task, due_date=None, complete=False, *contacts):
        self.task_list = [task]
        self.task = task
        self.due_date = due_date
        self.contacts = []
        self.complete = complete

    # if task has extra atributes (is complete, due date, contacts)
    # then these atributes are printed
    def __str__(self):
        print self.task
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

    #def add_task(self, task):


class Projects(object):

    def __init__(self):
        self.projects = {}

    # display project names
    def view_projects(self):
        x = 1
        for item in self.projects:
            print "%s.%s" %(x, item)
            x += 1

    # shows detailed view of single project
    def view_project(self, project_name):
        print self.projects.keys()
        x = 1
        for item in self.projects[project_name].task_list:
            print "%s. %s" % (x, item)
            x += 1
            if item.complete == True:
                print "    *COMPLETE*"
                # print self.task
            else:
                # print self.task
                if item.due_date != None and item.due_date != False:
                    print "    Due: %s" % item.due_date
                if item.contacts != None:
                    for name in item.contacts:
                        print "    > %s" % name
                    # print "     %s" % name.contact_name
                else:
                    pass

    # creats a project key but no task
    def create_project(self, project_name, task_one):
        self.projects[project_name] = Task(task_one)

    # creates task and adds it to the end of selected project
    def create_task(self, project_name, task):
        #new_task = Task(task)
        self.projects[project_name].task_list.append(task)

    # remove task indexed by project and by index
    def remove_task(self, project_name, task_del):
        del self.projects[project_name][task_del]

    # mark a task as complete
    def complete_task(self, project_name, task_complete):
        self.projects[project_name][task_complete].complete = True

    # change due date for task
    def due_task(self, project_name, due_task, new_due_date):
        self.projects[project_name][due_task].due_date = new_due_date

    # add contact to task
    def task_contact(self, project_name, task, contact):
        self.projects[project_name][task].contacts.append(contact)

    # remove contact from task
    def task_remove_contact(self, project_name, task, remove_contact):
        self.projects[project_name][task].contacts.pop(remove_contact)

# returns project name
def get_project():
    user.view_projects()
    get = raw_input("Select a project: ")
    return get

# returns project name, task index (int)
def get_task():
    x = get_project()
    user.view_project(x)
    select_task = int(raw_input("select task by number"))
    select_task -= 1
    # print select_task, x
    return x, select_task


def new_text():
    text = raw_input("enter something awesome: ")
    return text

def projects_menu():
    while True:
        print "PROJECTS MENU"
        print "1. new project"
        print "2. view projects"
        print "3. select a project"
        print "4. return to user menu"
        cmd = int(raw_input("make a selection: "))
        if cmd == 1:
            x = new_text()
            newt = raw_input("enter task number one: ")
            user.create_project(x, newt)
            single_project_menu(x)
        if cmd == 2:
            user.view_projects()
        if cmd == 3:
            single_project_menu(get_project())
        if cmd == 4:
            # user menu
            pass
        else:
            print "try harder"

def single_project_menu(y):
    user.view_project(y)
    print "what would you like to do with this project?"
    print "1. add a new task"
    print "2. edit a task"
    print "3. remove an project"
    print "4. view your project"
    print "5. return to projects menu"
    cmd = int(raw_input("make a selection: "))
    if cmd == 1:
        new_task = raw_input("enter new task: ")
        create_task(y, new_task)
    if cmd == 2:
        # get task
        # edit task menu
        pass
    if cmd == 3:
        user.view_project(y)
        rem_task = (int(raw_input("select task by number: ")) - 1)
        remove_task(y, rem_task)
    if cmd == 4:
        user.view_project(y)
    if cmd == 5:
        projects_menu()
    else:
        print "try harder"

#username.projects["projectname"].add_project()

user = Projects()
user.create_project("school", "test")

user.create_task("school", "homework")
user.create_task("school", "quiz")
#for item in user.projects["school"]:
 #   item.__str__()
#user.remove_task("school", 1)
#for item in user.projects["school"]:
 #   item.__str__()
#user.complete_task("school", 0)
#user.view_project("school")
projects_menu()
# user.add_project("school", new_task)