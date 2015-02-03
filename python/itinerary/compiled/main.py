#!/usr/bin/python
#

from addressbook import *
from calendar import *
from projects2 import *



class User(object):
    def __init__(self, name):
        self.name = name
        self.contacts = Addressbook()
        self.datebook = Date()
        self.projects = Projects()


#user = User('user')



    def main_menu(self, user):
        while True:
            print 'MAIN MENU'
            print '1. Contact'
            print '2. Appointment'
            print '3. Projects'
            print '4. Save'
            print '5. Quit'

            cmd = int(raw_input('make a selection by number > '))
            if cmd == 1:
                addr_menu(user)
            elif cmd == 2:
                date_menu(user)
            elif cmd == 3:
                projects_menu(user)
            elif cmd == 4:
                pass # pickle shit here
            elif cmd == 5:
                exit()
            else:
                print 'try harder '


user = User('user')

user.main_menu(user)
    
