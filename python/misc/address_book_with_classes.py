__author__ = 'student'
contact_list = {

}

class Contact():
    def __init__(self, first_name, last_name, business, phone, email, address):
        self.first_name = first_name
        self.last_name = last_name
        self.business = business
        self.phone = phone
        self.email = email
        self.address = address
    def display(self):
        print "** %s %s **" %(self.first_name, self.last_name)
        print self.business
        print "phone: " + self.phone
        print "email: " + self.email
        print "address: " + self.address
    def add_to_list(self):
        contact_list[self.first_name] = [self.first_name, self.last_name,
                                        self.business, self.phone, self.email,
                                        self.address]
        print contact_list
#    def into_ContactList(self):
#        self.ContactList = {self: [self.first_name, self.last_name,
#                                   self.business, self.phone, self.email,
#                                   self.address]}

#class ContactBook():
#   def __init__(self, Contact):
#        self.Contact = Contact
#    def show_all(self):
#        Contact.display(self)


#    def sort_by_last(self):
#    def sort_by_first(self):
def create_contact():
    new_first_name = raw_input("First Name: ")
    last_name = raw_input("Last Name: ")
    business = raw_input("Business or Relationship: ")
    phone = raw_input("Phone Number: ")
    email = raw_input("Email Address: ")
    address = raw_input("Street Adress: ")
    new_first_name = Contact(new_first_name, last_name, business, phone, email, address)
    new_first_name.display()
    new_first_name.add_to_list()
#    print contact_list

def Menu():
    choice = 99
    while choice != 0:
        print "**Contact Book**"
        print "To add a contact, press 1"
        print "To view your contacts, press 2"
        choice = raw_input("Make a selection: ")
        if choice == 1:
            create_contact()
            menu()
        if choice == 2:
            for key in contact_list:
                key.display()
                menu()
Menu()
"""
alex = Contact("alex", "tryon",
               "student: code-guild",
               "5034078855",
               "alextryonpdx@gmail.com",
               "1021 N Bryant")


alex.add_to_list()
create_contact()

"""