__author__ = 'student'
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

#    def sort_by_last(self):
#    def sort_by_first(self):
def create_contact():
    new_first_name = raw_input("First Name: ")
    last_name = raw_input("Last Name: ")
    business = raw_input("Business or Relationship: ")
    phone = raw_input("Phone Number")
    email = raw_input("Email Address: ")
    address = raw_input("Street Adress: ")
    new_first_name = Contact(new_first_name, last_name, business, phone, email, address)
    new_first_name.display()

alex = Contact("alex", "tryon",
               "student: code-guild",
               "5034078855",
               "alextryonpdx@gmail.com",
               "1021 N Bryant")

create_contact()