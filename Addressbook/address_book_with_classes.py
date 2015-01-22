__author__ = 'student'
"""
second attempt at contact list program employing classes.
classes are still confusing me so i need more practice
currently the list class is home for all functions, there should be a better way
also first attempt at pickle module. seems straightforward but stupid

"""

# Contact Class takes a buncha inputs and has a function to display the data
# contacts are stored by first name
# this could and should be changed to full name to facilitate better search
# but it needs to be changed in the ContactList class

class Contact(object):
    def __init__(self, first_name, last_name, business, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.business = business
        self.phone = phone
        self.email = email
        self.address = address

# overrides print function in the case of any contact instance
    def __str__(self):
         print "** %s %s ** \n %s \n %s \n %s \n %s" % (self.first_name,
                self.last_name, self.business, self.phone, self.email,
                self.address)




class ContactList(object):
    def __init__(self):
        self.contact_list = {}

# function to add contact to contact list
    def add_contact(self):
        first_name = raw_input("First Name: ")
        last_name = raw_input("Last Name: ")
        business = raw_input("Business or Relationship: ")
        phone = raw_input("Phone Number: ")
        email = raw_input("Email Address: ")
        address = raw_input("Street Adress: ")
        new_contact = Contact(first_name, last_name, business, phone, email, address)
        self.contact_list[new_contact.first_name] = new_contact
        new_contact.__str__()
        confirm = raw_input("Save new contact? y/n ")
        if confirm == "y":

            open_contacts = open("contacts.pk1", "wb")
            pickle.dump(self.contact_list, open_contacts)
        else:
            back_to_menu = raw_input("enter to continue")
            menu()

# pulls data from save file and populates contact list
    def load_contacts(self):

        open_contacts = open("contacts.pk1", "rb")
        saved_contacts = pickle.load(open_contacts)
        self.contact_list = saved_contacts
        return self.contact_list
     #   return saved_contacts

    def save_contacts(self):
        pickle.dump(self.contact_list, open("contacts.pk1", "wb"))

    def view_contacts(self):
#        ContactList.load_contacts(self)
        for item in self.contact_list:
            self.contact_list[item].__str__()

     #   self.contact_list = saved_contacts
      #  for item in self.contact_list:
      #  self.contact_list.__str__

# search currently requires exact match to pull contact
# having trouble iterating through contacts via keys in ContactList dict
# WHY!?!?!?!?

    def search(self):
#        ContactList.load_contacts(self)
        search_name = raw_input("Who are you searching for?")
        print search_name
      #  for key in self.contact_list:
        if search_name in self.contact_list:
            self.contact_list[search_name].__str__()
        else:
            print "No contact found by that name."
            search_again = raw_input("Would you like to search again? y/n ")
            if search_again.lower() == "y":
                self.search()
            else:
                back_to_menu = raw_input("enter to continue")
                menu()

    def erase_contact(self):
#        ContactList.load_contacts(self)
        erase_name = raw_input("Which contact would you like to erase?")
        print erase_name
        if erase_name in self.contact_list:
            self.contact_list[erase_name].__str__()
            erasure = self.contact_list[erase_name]
            confirm_erase = raw_input("Would you like to erase this contact? y/n")
            if confirm_erase == "y":

                open_contacts = open("contacts.pk1", "wb")
                del self.contact_list[erase_name]
                pickle.dump(self.contact_list, open("contacts.pk1", "wb"))
                self.view_contacts()
                back_to_menu = raw_input("enter to continue")
                menu()
            else:
                self.view_contacts()
                back_to_menu = raw_input("enter to continue")
                menu()
        else:
            self.view_contacts()


       # for item in self.contact_list:
        #    if search_name in self.contact_list[item]:
         #       self.contact_list[item].__str__()
         #   else:
          #      pass


# Erase can be fixed when search and file IN/OUT are both refined
# need more pickle research
"""
    def erase(self):
        ContactList.search(self)
        del self.contact_list[searched]
        import pickle
        open_contacts = open("contacts.pk1", "wb")
        pickle.dump(self.contact_list, open_contacts)
        self.contact_list.load_contacts()
        self.contact_list.view_contacts()
"""
     #       else:
      #          pass
#ContactList.load_contacts()
# first or last = raw_input("search by first or last name?")
# who = raw_input("what is the search name?")
# if first_or_last == first:
    #
import pickle
def menu():
    test_contacts = ContactList()
    test_contacts.load_contacts()
    print "1. View Contacts"
    print "2. Search Contacts"
    print "3 Add a Contact"
    print "4 Delete a Contact"
    print "5. Save and Exit"
    menu_choice = raw_input("select an option by number: ")
    if menu_choice == "1":
        test_contacts.view_contacts()
    if menu_choice == "2":
        test_contacts.search()
    if menu_choice == "3":
        test_contacts.add_contact()
    if menu_choice == "4":
        test_contacts.erase_contact()
    if menu_choice == "5":
        if raw_input("are you sure? y/n") == "y":
            test_contacts.save_contacts()
            exit()
        else:
            menu()
    else:
        menu()

menu()
# testing function-calls and a loop for some other tests.

#test_contacts = ContactList()
#test_contacts.load_contacts()
#test_contacts.view_contacts()
#test_contacts.add_contact()
#test_contacts.add_contact()
#test_contacts.erase_contact()
# when sending "searched" variable to global, it causes problems because duh
# searched = ""

#test_contacts.add_contact()
#test_contacts.load_contacts()
#x = 10
#while x == 10:
    #test_contacts.load_contacts()
    #test_contacts.add_contact()
  #  test_contacts.view_contacts()
 #   x += 10
 #  test_contacts.erase()