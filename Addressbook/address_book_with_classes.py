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
            import pickle
            open_contacts = open("contacts.pk1", "wb")
            pickle.dump(self.contact_list, open_contacts)
        # else: send to menu

# pulls data from save file and populates contact list
    def load_contacts(self):
        import pickle
        open_contacts = open("contacts.pk1", "rb")
        saved_contacts = pickle.load(open_contacts)
        self.contact_list = saved_contacts
        return self.contact_list
     #   return saved_contacts


    def view_contacts(self):
        ContactList.load_contacts(self)
        for item in self.contact_list:
            self.contact_list[item].__str__()
     #   self.contact_list = saved_contacts
      #  for item in self.contact_list:
      #  self.contact_list.__str__

# search currently requires exact match to pull contact
# having trouble iterating through contacts via keys in ContactList dict
# WHY!?!?!?!?
    def search(self):
        ContactList.load_contacts(self)
        search_name = raw_input("Who are you searching for?")
        print search_name
        if search_name in self.contact_list:
            self.contact_list[search_name].__str__()
            searched = self.contact_list[search_name]
            global searched
        else:
            pass
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



# testing function-calls and a loop for some other tests.

test_contacts = ContactList()

# when sending "searched" variable to global, it causes problems because duh
searched = ""

#test_contacts.add_contact()
#test_contacts.load_contacts()
#x = 10
#while x == 10:
    #test_contacts.load_contacts()
    #test_contacts.add_contact()
  #  test_contacts.view_contacts()
 #   x += 10
test_contacts.erase()