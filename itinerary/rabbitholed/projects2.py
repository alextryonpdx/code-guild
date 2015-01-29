class Task(object):
    def __init__(self, task, due_date=None, complete=False, *contacts):
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
        for item in self.projects[project_name]:
            item.__str__()

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
        self.projects[project_name][task].contacts.pop(remove_contact)



#username.projects["projectname"].add_project()

test = Projects()
test.create_project("school")

test.create_task("school", "homework")
test.create_task("school", "quiz")
for item in test.projects["school"]:
    item.__str__()
test.remove_task("school", 1)
for item in test.projects["school"]:
    item.__str__()
test.view_projects()
# test.add_project("school", new_task)