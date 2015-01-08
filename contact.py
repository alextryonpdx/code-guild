



book = {
"test": {
	"phone":"test",
	"full_name":"test_name",
	"address":"123 test",
	"email":"test@internet.com"},
"deleter": {
	"phone":"444",
	"full_name":"test_name",
	"address":"456 test",
	"email":"gogogo@google.com"},
}

	

print "***********WELCOME TO YOUR CONTACT BOOK***********"

user_task = raw_input("would you like to View(v), Edit(e), Create(c), or Delete(d) your contacts?")
user_task = user_task.lower()
acceptible_input = ('view','v','delete','d','edit','e','create','c')

if user_task in acceptible_input[:2]:
	print book

if user_task in acceptible_input[2:4]:
	contact_to_delete = raw_input("which contact would you like to delete?")
	print "delete contact %s ?" %(contact_to_delete)
	delete_confirmation = raw_input("enter y or n:")
	if delete_confirmation == "y":
		del book[contact_to_delete]
		print book

if user_task in acceptible_input[4:6]:
	user_to_edit = raw_input("which user would you like to edit?")
	phone_confirm = raw_input("Would you like to change %s 's phone number? y or n" %(user_to_edit))
	if phone_confirm == "y":
		new_phone = raw_input("What is the new phone number for this %s ?" %(user_to_edit))
	address_confirm = raw_input("Would you like to change the address for this %s ?  y or n:" %(user_to_edit))
	if address_confirm == "y":
		new_address = raw_input("what is the new address for %s ?" %(user_to_edit))
	email_confirm = raw_input("Would you like to change the email address for %s ?   y or n" %(user_to_edit))	
	if email_confirm == "y":
		new_email = raw_input("What is the new email address for %s ?" %(user_to_edit))


	print book

if user_task in acceptible_input[6:8]:
	name_key = raw_input("To create a new contact, enter a first name:")
	full_name = name_key + raw_input("What is your contact's last name?")
	phone = raw_input("What is this contact's primary phone number?")
	option_phone = raw_input("Does this contact have a secondary phone number?  y or n: ")
	if option_phone == "y":
		secondary_phone = raw_input("What is this contact's secondary phone number?")
	address = raw_input("What is this contact's address?")
	email = raw_input("What is this contact's email address?")
	confirm_add = raw_input("Add contact: %s ?... y or n?" %(full_name))
	if confirm_add == "y":
			book[name_key] = {"phone:": phone, "full name:" : full_name, "address:": address, "email:": email}

	print book
	

