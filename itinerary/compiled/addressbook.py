#!/usr/bin/python
# Addressbook v2
# Matthew Long







class Contact(object):
    def __init__(self, first, last, ph1, ph2=None, 
                 email=None, addr=None, url=None):

        self.first = first
        self.last = last
        self.ph1 = ph1
        self.ph2 = ph2
        self.email = email
        self.addr = addr
        self.url = url
        self.fullname = self.first + " " + self.last



class Addressbook(object):

    def __init__(self):
        self.contacts = {}
    

    def view(self, fullname):
        name = fullname
        print('\n')
        print('first name: %s' % self.contacts[name].first)
        print('last name: %s' % self.contacts[name].last)
        print('phone: %s' % self.contacts[name].ph1)
        print('phone 2: %s' % self.contacts[name].ph2)
        print('email address: %s' %self.contacts[name].email)
        print('address: %s' %self.contacts[name].addr)
        print('url: %s' % self.contacts[name].url)
        print('\n')

     
    def edit(self, fullname, arg, value):
        name = fullname
        if arg == 'phone':
            self.contacts[name].ph1 = value
        elif arg == 'phhone2':
            self.contacts[name].ph2 = value
        elif arg == 'email':
            self.contacts[name].email = value
        elif arg == 'address':
            self.contacts[name].addr = value
        elif arg == 'url':
            self.contacts[name].url = value
        else:
             print('try again..')

    
    def delete(self, fullname):
        name = fullname
        del self.contacts[name]

    
    def addcontact(self, first, last, ph1, ph2=None,
                   email=None, addr=None, url=None):

        new_contact = Contact(first, last, ph1, ph2, email, addr, url)
        self.contacts[new_contact.fullname] = new_contact



    def listcontacts(self):
        for key in self.contacts:
            print('\n')
            print(key)
        print('\n')


    def showall(self):
        print('\n')
        for key in self.contacts:
            self.view(key)
            print('\n')




def addr_menu(user):

   # user = Addressbook()
    

    def add_new(user):
        f = raw_input('\nEnter a first name >> ')
        l = raw_input('\nEnter a a last name >> ')
        p1 = raw_input('\nEnter a phone number >> ')
        p2 = raw_input('\nEnter another phone number >> ')
        e = raw_input('\nEnter an email address >> ')
        ad = raw_input('\nEnter an address >> ')
        u = raw_input('\nEnter a url >> ')

        user.contacts.addcontact(f, l, p1, p2, e, ad, u)




    def delete_entry(user):
        user.contacts.listcontacts()
        d = raw_input('\nEnter a person to delete >> ')
        user.contacts.delete(d)



    def edit_entry(user):
        user.contacts.listcontacts()
        name = raw_input('\nWho would you like to edit? >> ') 
        print('\n\nphone, phon2, email, address, url')       
        what = raw_input('\n\nWhat would you like to edit? >> ')    
        val = raw_input('\nWhat would you like to change it to? >> ')

        user.contacts.edit(name, what, val)



    def view_contact(user):
        user.contacts.listcontacts()
        name = raw_input('\n\nWho would you like to view? >> ')
        user.contacts.view(name)



 
    while True:
        print('\n\nEnter a command: add, edit, delete, view, list, showall, quit')
        cmd = raw_input('\n\n>>>>> ')
        if cmd == 'add':
            add_new(user)
        elif cmd == 'delete':
            delete_entry(user)
        elif cmd == 'edit':
            edit_entry(user)
        elif cmd == 'view':
            view_contact(user)
        elif cmd == 'list':
             user.contacts.listcontacts(user)
        elif cmd == 'showall':
             user.contacts.showall(user)
        elif cmd == 'quit':
             user.main_menu(user)
        else:
            print('\n\nTRY HARDER\n\n')



#menu()

 








