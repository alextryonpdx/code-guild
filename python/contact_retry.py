# empty dictionary for contact list

contact_list= dict(alex={
	'nickname:': 'alex',
	'name:': 'Alex Tryon',
	'ph1:': '(503)407-8855',
	'ph2:': 'n/a',
	'email:': 'alextryonpdx@gmail.com',
	'address:': '1021 N Bryant'}, suzie={
'nickname:': 'suzie',
'name:': 'Suzie Tryon',
'ph1:': '(503)407-9323',
'ph2:': '(503)524-9269',
'email:': 'suzie.tryon@comcast.net',
'address:': '11763 SW Swendon Loop'})
menu_choice = '0'
while menu_choice != '6':
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
	print '\n'

# display full contact book. formatted with blank line between each contact
	if menu_choice == '1':
		for i in contact_list.keys():
			print "\n"
			print contact_list[i]['nickname:']
			print 'name:' + ' ' + contact_list[i]['name:']
			print 'ph1:' + ' ' + contact_list[i]['ph1:']	
			print 'ph2:' + ' ' + contact_list[i]['ph2:']
			print 'ph3:' + ' ' + contact_list[i]['email:']
			print 'address:' + ' ' + contact_list[i]['address:']
			


		# if menu_choice == '2':
	if menu_choice == '2':
		search = raw_input('Which contact are you looking for?')
		search = search.lower()
		if search in contact_list:
			print "\n"
			print 'name:' + ' ' + contact_list[search]['name:']
			print 'ph1:' + ' ' + contact_list[search]['ph1:']	
			print 'ph2:' + ' ' + contact_list[search]['ph2:']
			print 'email:' + ' ' + contact_list[search]['email:']
			print 'adrs:' + ' ' + contact_list[search]['address:']
			print "\n"
		else:
			print "No contact found by that name"
				

	if menu_choice == '3':
		new_nickname = raw_input("What is your new contact's nickname?")
		new_nickname = new_nickname.lower()
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
			contact_list[new_nickname] = {'nickname:': new_nickname, 'name:' : new_name, 'ph1:': new_phone1, 'ph2:':new_phone2, 'email:': new_email, 'address:':new_address}
			print "\n"
			print new_nickname
			print 'name:' + ' ' + contact_list[new_nickname]['name:']
			print 'ph1:' + ' ' + contact_list[new_nickname]['ph1:']	
			print 'ph2:' + ' ' + contact_list[new_nickname]['ph2:']
			print 'email:' + ' ' + contact_list[new_nickname]['email:']
			print 'adrs:' + ' ' + contact_list[new_nickname]['address:']
		#	f = open('list.txt', 'w')
		#	f.write(contact_list[new_nickname:['name':new_name, 'ph1': new_phone1, 'ph2': new_phone2, 'email': new_email, 'address': new_address]])
		#	f.close()
			
		else:
			print "\n New contact forgotten"
		

	if menu_choice == '6':
		quit()
