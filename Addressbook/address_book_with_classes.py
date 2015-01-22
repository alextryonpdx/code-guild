__author__ = 'student'
"""
second attempt at contact list program employing classes.
classes are still confusing me so i need more practice
currently the list class is home for all functions, there should be a better way
also first attempt at pickle module. seems straightforward

To-Do manage user experience, repetitive input requests, input controls, etc
      clean up overall display. uuuuuuuugly
"""

import pickle
import os

# Contact Class takes a buncha inputs and has a function to display the data
# contacts are stored by first name
# this could and should be changed to full name to facilitate better search
# but it needs to be changed in the ContactList class


class Contact(object):
    """
    Contact class requires many inputs. only defined function is to display.
    Contact indexed in ContactList by first name
    """
    def __init__(self, first_name, last_name, business, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.business = business
        self.phone = phone
        self.email = email
        self.address = address

    # overrides print function for contact instance
    def __str__(self):
         print "** %s %s ** \n %s \n phone: %s \n email: %s \n address: %s" \
               % (self.first_name, self.last_name, self.business, self.phone,
                  self.email, self.address)




class ContactList(object):
    """
    ContactList class responsible for bulk of functionality:
        create, delete, search for, view all
    ContactList is a dictionary. In case of Contact, it is indexed by first name
    """
    def __init__(self):
        self.contact_list = {}

    # function to add contact to contact list
    # User is prompted for each piece of data for contact
    # contact is created then stored by first name
    # TO-DO set "n/a" as default value for every input besides name
    # TO-Do INPUT CONTROL!!!!!!!
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
        # if user confirms save:
        # external contacts.pk1 file is rewritten with updated dictionary
        if confirm == "y":
            open_contacts = open("contacts.pk1", "wb")
            pickle.dump(self.contact_list, open_contacts)
            back_to_menu = raw_input("Contact Saved. enter to continue")
        # if anything but "y" input, user prompted for return to menu
        else:
            back_to_menu = raw_input("enter to continue")
            menu()

    # pulls data from save file and populates contact list
    # function only employed at start of program (menu)
    def load_contacts(self):
        open_contacts = open("contacts.pk1", "rb")
        saved_contacts = pickle.load(open_contacts)
        self.contact_list = saved_contacts
        return self.contact_list

    # updates contacts.pk1 with new dictionary
    # function employed at end of other functions that make changes to dict
    def save_contacts(self):
        pickle.dump(self.contact_list, open("contacts.pk1", "wb"))

    # iterates through contact list and calls __str__ for each Contact instance
    def view_contacts(self):
        for item in self.contact_list:
            self.contact_list[item].__str__()
        raw_input("enter to continue")

    # search currently requires exact match to pull contact
    # in case of exact match, contact instance __str__ is called
    # if no match made, option for new search or return to main menu
    def search(self):
        search_name = raw_input("Who are you searching for?")
        print search_name
        if search_name in self.contact_list:
            self.contact_list[search_name].__str__()
            raw_input("enter to continue")
        else:
            print "No contact found by that name."
            search_again = raw_input("Would you like to search again? y/n ")
            if search_again.lower() == "y":
                self.search()
            else:
                back_to_menu = raw_input("enter to continue")
                menu()

    # employs structure of search function, has same issues (see above)
    # if contact found, used prompted to confirm deletion
    # contact remove from dict by key(first name)
    # updated dict saved to contacts.pk1
    # if no confirm, view_contacts called, return to menu
    # if no match, new search or return to menu options
    def erase_contact(self):
        erase_name = raw_input("Which contact would you like to erase?")
        print erase_name
        if erase_name in self.contact_list:
            self.contact_list[erase_name].__str__()
            confirm_erase = raw_input("Would you like to erase this contact? y/n")
            if confirm_erase == "y":
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

# basic function used in stages of program to clear screen
def clear_screen():
    os.system("clear")

# menu holds structure for program
# main control center
# TO-DO could use some input control
def menu():
    clear_screen()
    test_contacts = ContactList()
    test_contacts.load_contacts()
    print "Contact Book"
    print "\n" * 5
    print "1. View Contacts"
    print "2. Search Contacts"
    print "3. Add a Contact"
    print "4. Delete a Contact"
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
