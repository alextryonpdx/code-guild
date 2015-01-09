# empty dictionary for contact list

contact_list={
'Alex':{
'name:':'Alex Tryon,',
'ph1:':'(503)407-8855', 
'ph2:':'n/a', 
'email:' :'alextryonpdx@gmail.com', 
'address:':'1021 N Bryant'}, 
'Suzie': {
'name:':'Suzie Tryon',
'ph1:':'(503)407-9323', 
'ph2:':'(503)524-9269',
'email:':'suzie.tryon@comcast.net', 
'address:':'11763 SW Swendon Loop'}
}


# MENU SCREEN
"""menu_choice = '0'
while  menu_choice is not '6'"""
print "CONTACTS!"
print "OPTIONS:"
print "1. View contact list"
print "2. Find contact"
print "3. Create new contact"
print "4. Edit an existing contact"
print "5. Delete a contact"
print "6. Exit"
menu_choice = raw_input("What would you like to do?")
"""
non-working failsafe menu retry in case of impropper user input
##### install at end of program as "else" loop?

while menu_choice is not in ['1','2','3','4','5','6']:
	print "\n"*5
	print "Please review selections and enter corresponding number:"
	print "OPTIONS:"
	print "1. View contact list"
	print "2. Find contact"
	print "3. Create new contact"
	print "4. Edit an existing contact"
	print "5. Delete a contact"
	print "6. Exit"
	menu_choice = raw_input("What would you like to do?")
else:
"""



# display full contact book. formatted with blank line between each contact
if menu_choice == '1':
	for i in contact_list.keys():
		print "\n"
		print 'name:' + ' ' + contact_list[i]['name:']
		print 'ph1:' + ' ' + contact_list[i]['ph1:']	
		print 'ph2:' + ' ' + contact_list[i]['ph2:']
		print 'ph3:' + ' ' + contact_list[i]['email:']
		print 'adrs:' + ' ' + contact_list[i]['address:']
	print "\n"


	# if menu_choice == '2':

if menu_choice == '3':
	new_nickname = raw_input("What is your new contact's nickname?")
	new_name = raw_input("What is %s's full name?"%(new_nickname))
	new_phone1 = raw_input("what is %s's phone number?"%(new_nickname))
	phone2_option = raw_input("Does %s have a second phone number? (y , n)"%(new_nickname))
	if phone2_option.lower() == 'y':
		new_phone2 = raw_input("What is %s's second phone number?"%(new_nickname))
	else:
		new_phone2 = 'n/a'
	new_email = raw_input("What is %s's email address?"%(new_nickname))
	new_address = raw_input("What is %s's address?"%(new_nickname))
	confirm_add = raw_input("Add %s as new contact? (y , n)"%(new_nickname))
	if confirm_add == 'y':
		contact_list[new_nickname] = [new_name, new_phone1, new_phone2,new_email,new_address]
		print "\n"
		print new_nickname
		print contact_list[new_nickname][0]
		print contact_list[new_nickname][1]	
		print contact_list[new_nickname][2]
		print contact_list[new_nickname][3]
		print contact_list[new_nickname][4]
	else:
		print "\n New contact forgotten"
	

if menu_choice == '6':
	quit()
