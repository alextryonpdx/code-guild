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
            user.projects.__str__()
            #print user.projects.project_name

    def pickle_users(self,username):
        pickle.dump(self.args, open("un_pw.pk1", "wb"))

    def unpickle_users(self):
        self.args = pickle.load(open("un_pw.pk1", "rb"))

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
                    user.user_menu(user.username, user.projects)
            else:
                print "password and username do not match"
                self.start_menu()

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
            # appointments = AppointmentBook(username)
            username = User(username, password, projects)
            self.args.append(username)
            self.pickle_users(username)
            self.__str__()
            print "New user account created."
            print "please login"
            self.start_menu()

    # TOP LOGIN MENU
    #SENDS USER TO LOGIN OR CREATE USER FUNCTION
    def start_menu(self):
        self.unpickle_users()
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