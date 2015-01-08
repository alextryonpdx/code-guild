
"""
CONTACT LIST PROGRAM
USER has contact list defined which they may add to, edit, view, or delete.
current state of contact list is printed at end of each loop
program ends at end of loop of each function

TO Do:
-find a better way to display the contact list!!!!!
-find way to keep program running, updating list:
	-without exiting after single function is complete
	
-need to control user inputs throughout program:
			-force lowercase
				*employed .lower() function on confirmations
			-confirm alpha/num entries
			-ask for re-entry after improper user entries
"""

# initial list stored as nested dictionary to allow maximum mutability/index access

book = {
"test": {
	"phone":"123",
	"full_name":"test_name",
	"address":"123 test st",
	"email":"test@internet.com"},
"deleter": {
	"phone":"999",
	"secondary phone": "888",
	"full_name":"deletable",
	"address":"456 test st",
	"email":"gogogo@google.com"},
}

	
# Opening MENU screen USER will see:

print "***************************WELCOME TO YOUR CONTACT BOOK***************************"
user_task = raw_input("would you like to View(v), Edit(e), Create(c), Delete(d) or Quit(q) your contacts?")
user_task = user_task.lower()
acceptible_input = ('view','v','delete','d','edit','e','create','c', 'q', 'quit')

# USER sent to one of four functions or asked to re-enter selection in case of wrong entry


# quit function using "if-in"
if user_task in ("q","quit"):
		quit()

# WHILE loop returns USER to menu in case of improper entry
while user_task not in acceptible_input:
	print "***************************WELCOME TO YOUR CONTACT BOOK***************************"
	print "**************************Please re-enter your selection**************************"
	user_task = raw_input("would you like to View(v), Edit(e), Create(c), Delete(d) or Quit(q) your contacts?")
	user_task = user_task.lower()
	acceptible_input = ('view','v','delete','d','edit','e','create','c')
# quit function using "if-in"
	if user_task in ("q","quit"):
		quit()

"""
this is the view functionality
users can view the current state of their contact list
"""

if user_task in acceptible_input[:2]:
	print book


"""
this is the delete functionality
user types the name of contact entry to delete
user then confirms intent to delete entry
after confirmation, entry is deleted and updated contact list is displayed
"""
if user_task in acceptible_input[2:4]:
	contact_to_delete = raw_input("which contact would you like to delete?")
	# confirming that the user wants to delete the chosen entry
	print "delete contact %s ?" %(contact_to_delete)
	delete_confirmation = raw_input("enter y or n:")
	# delete the chosen contact
	if delete_confirmation.lower() == "y":
		del book[contact_to_delete]
		print book



"""
this is the EDIT contact functionality
user enters contact they intend to edit
user is asked which parts of contact to edit(last name, phone, address, email)
user enters new information and skips information that is not to be editted
new contact is displayed for confirmation before updating the contact list
new complete contact list is displayed
"""
if user_task in acceptible_input[4:6]:
	user_to_edit = raw_input("which user would you like to edit?")
	if user_to_edit in book.keys():
		full_name = user_to_edit + " " + raw_input("What is %s's last name?" %(user_to_edit))
		# check for EDIT of PHONE, if "y", store new phone
		phone_confirm = raw_input("Would you like to change %s 's phone number? y or n: " %(user_to_edit))
		if phone_confirm.lower() == "y":
			new_phone = raw_input("What is the new phone number for %s ?" %(user_to_edit))
		else:
			new_phone = book[user_to_edit]["phone"]
		# check for EDIT of SECONDARY PHONE, if "y", store new phone
		secondary_phone_confirm = raw_input("Would you like to change the secondary phone number for %s ? y or n?" %(user_to_edit))
		if secondary_phone_confirm.lower() == "y":
			new_secondary_phone = raw_input("What is the new secondary phone number for %s ?" %(user_to_edit))
		else:
			new_secondary_phone = "n/a"
		# check for EDIT of ADDRESS, if "y", store new address
		address_confirm = raw_input("Would you like to change the address for this %s ?  y or n: " %(user_to_edit))
		if address_confirm.lower() == "y":
			new_address = raw_input("what is the new address for %s ?" %(user_to_edit))
		else:
			new_address = book[user_to_edit]["address"]
		# check for EDIT of EMAIL, if "y", store new address
		email_confirm = raw_input("Would you like to change the email address for %s ?   y or n: " %(user_to_edit))	
		if email_confirm.lower() == "y":
			new_email = raw_input("What is the new email address for %s ?" %(user_to_edit))
		else:
			new_email = book[user_to_edit]["email"]
		if raw_input("Confirm new contact information: full name: %s, phone: %s, secondary phone: %s, address: %s, email:%s? y or n:" %(full_name, new_phone, new_secondary_phone, new_address, new_email)) == "y":
			book[user_to_edit] = {"full name:": full_name, "phone:": new_phone, "secondary phone:": new_secondary_phone, "address:": new_address, "email:":new_email}
	# if non-existant contact is entered, EDIT function is broken. Find way to restart program
	else:
		print "No contact found with the name %s."	%(user_to_edit)

	print book

"""
this is NEW CONTACT functionality
step-by-step USER enters information for new entry
	-no form of control for information entered by USER. 
		-not problematic from programming standpoint
		-could increase usability potentially if remedied
"""
if user_task in acceptible_input[6:8]:
	name_key = raw_input("To create a new contact, enter a first name:")
	full_name = name_key + " " + raw_input("What is your contact's last name?")
	phone = raw_input("What is this contact's primary phone number?")
	option_phone = raw_input("Does this contact have a secondary phone number?  y or n: ")
	if option_phone.lower() == "y":
		secondary_phone = raw_input("What is this contact's secondary phone number?")
	else:
		secondary_phone = "n/a"
	address = raw_input("What is this contact's address?")
	email = raw_input("What is this contact's email address?")
	confirm_add = raw_input("Add contact: %s?... y or n?" %(full_name))
	if confirm_add.lower() == "y":
			book[name_key] = {"full name:" : full_name, "phone:": phone, "secondary phone:": secondary_phone,"address:": address, "email:": email}

	print book
	

