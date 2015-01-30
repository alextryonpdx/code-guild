

class Task(object):
    def __init__(self, task, due_date=None, complete=False, *contacts):
        self.task_list = [task]
        self.task = task
        self.due_date = due_date
        self.contacts = []
        self.complete = complete

    # if task has extra attributes (is complete, due date, contacts)
    # then these attributes are printed
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


class Projects(object):

    def __init__(self):
        self.projects = {}

    # display project names
    def view_projects(self):
        for item in self.projects:
            print "%s" % item

    # shows detailed view of single project
    def view_project(self, project_name):
        print "* %s *" % project_name
        x = 1
        for item in self.projects[project_name]:
            print "%s. %s" % (x, item.task)
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
    def create_project(self, project_name):
        self.projects[project_name] = []

    # creates task and adds it to the end of selected project
    def create_task(self, project_name, task):
        new_task = Task(task)
        self.projects[project_name].append(new_task)

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
        self.projects[project_name][task].contacts.remove(remove_contact)


# returns project name
def get_project(user):
    user.projects.view_projects()
    get = raw_input("Select a project by name: ")
    return get

# returns project name, task index (int)
def get_task(user, y=None):
    if y:
        pass
    else:
        y = get_project(user)
    user.projects.view_project(y, user)
    select_task = int(raw_input("select task by number"))
    select_task -= 1
    # print select_task, x
    return y, select_task, user


def new_text():
    text = raw_input("enter something awesome: ")
    return text

def projects_menu(user):
    while True:
        print "PROJECTS MENU"
        print "1. new project"
        print "2. view projects"
        print "3. select a project"
        print "4. return to user menu"
        cmd = int(raw_input("make a selection: "))
        if cmd == 1:
            x = new_text()
            # newt = raw_input("enter task number one: ")
            user.projects.create_project(x)
            single_project_menu(x, user)
        if cmd == 2:
            user.projects.view_projects()
            cont = raw_input("enter to continue...")
            projects_menu(user)
        if cmd == 3:
            single_project_menu(get_project(user))
        if cmd == 4:
            user.main_menu(user)
        else:
            print "try harder"

def single_project_menu(y, user):
    user.projects.view_project(y)
    print "what would you like to do with this project?"
    print "1. add a new task"
    print "2. edit a task"
    print "3. remove an project"
    print "4. view your project"
    print "5. return to projects menu"
    cmd = int(raw_input("make a selection: "))
    if cmd == 1:
        new_task = raw_input("enter new task: ")
        user.projects.create_task(y, new_task)
    if cmd == 2:
        y, edit = get_task(user, y)
        edit_task_menu(y, edit)
        pass
    if cmd == 3:
        user.view_project(y)
        rem_task = (int(raw_input("select task by number: ")) - 1)
        remove_task(y, rem_task)
    if cmd == 4:
        user.projects.view_project(y)
    if cmd == 5:
        projects_menu(user)
    else:
        single_project_menu(y, user)    

def edit_task_menu(user, y, edit):
    while True:
        if len(user.projects.projects) == 0:
            print "nothing to see here"
            single_project_menu(y, user)
        else:
            print "1. remove this task\n" \
                  "2. change the due date for this task\n" \
                  "3. add a contact to this task\n" \
                  "4. remove a contact from this task\n" \
                  "5. mark this task as COMPLETE\n" \
                  "6. return to project menu"
            cmd = int(raw_input("make a selection: "))
            if cmd == 1:
                user.projects.remove_task(y, edit)
                single_project_menu(y, user)
            if cmd == 2:
                new_due_date = raw_input("when is this task due? DD-MM-YY ")
                user.projects.due_task(y, edit, new_due_date)
            if cmd == 3:
                contact = raw_input("which contact would you like to add? ")
                user.projects.task_contact(y, edit, contact)
            if cmd == 4:
                contact = raw_input("remove which contact?")
                user.projects.task_remove_contact(y, edit, contact)
            if cmd == 5:
                user.projects.complete_task(y, edit)
            if cmd == 6:
                single_project_menu(y, user)
            else:
                edit_task_menu(y, edit, user)


"""
#username.projects["projectname"].add_project()

#user = Projects()
#user.create_project("school")

#user.create_task("school", "homework")
#user.create_task("school", "quiz")
#for item in user.projects["school"]:
 #   item.__str__()
#user.remove_task("school", 1)
#for item in user.projects["school"]:
 #   item.__str__()
#user.complete_task("school", 0)
#user.view_project("school")
#projects_menu()
# user.add_project("school", new_task)

"""
