__author__ = 'student'
contact_list = {"alex": ["alex", "tryon",
               "student: code-guild",
               "5034078855",
               "alextryonpdx@gmail.com",
               "1021 N Bryant"], }



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
    def save(self, first_name, last_name, business, phone, email, address):
        contact_list[first_name] = [first_name, last_name, business,
                                    phone, email, address]
# test        print contact_list

"""
def show_all_contacts():
    for keys in contact_list[::]:
        contact.display()
"""

#    def sort_by_last(self):
#    def sort_by_first(self):
def create_contact():
    first_name = raw_input("First Name: ")
    last_name = raw_input("Last Name: ")
    business = raw_input("Business or Relationship: ")
    phone = raw_input("Phone Number")
    email = raw_input("Email Address: ")
    address = raw_input("Street Adress: ")
    new_contact = Contact(first_name, last_name,
                             business, phone, email,
                             address)
#    new_first_name.display()
    save = raw_input("save contact? y,n: ")
    if save == "y":
        new_contact.save(first_name, last_name, business, phone, email, address)
    else:
        print "Contact Discarded"
"""
def save_contact(new_first_name):
    add_to_book = open("addressbook.txt", "w")
    for item in new_first_name():
        add_to_book.write(str(item) + " ")
        add_to_book.close()
"""



alex = Contact("alex", "tryon",
               "student: code-guild",
               "5034078855",
               "alextryonpdx@gmail.com",
               "1021 N Bryant")

create_contact()