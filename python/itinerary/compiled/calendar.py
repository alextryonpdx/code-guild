#!/usr/bin/python
# Matthew Long

# this should be created in the user class
#user = Date()




class Date(object):
    def __init__(self):
        self.date = {}

 
    def adddate(self, date):
        self.date[date] = Event()

 
#    def adddate(self, year, month, day):
#        self.year = year
#        self.month = month
#        self.day = day
#        self.name = self.year + self.month + self.day
#        self.date[self.name] = Day()


    def deldate(self, day):
        del self.date[day]


    def showdays(self):
        for keys in self.date:
            print(keys)



    

class Event(object):
    def __init__(self):
        self.events = {}

    
    def addevent(self, hour, event):
        self.events[hour] = event


    def delevent(self, hour):
        del self.events[hour]


    def editevent(self, hour, event):
        self.events[hour] = event 


    def showevents(self):
        for k, v in self.events:
            print(k, v)



#user = Date()

def date_menu(user):
    print(' %%% Appointment Book %%% ')

    def getdate():
        date = raw_input('Enter a date, DD-MM-YY >>> ')
        return date

    def gettime():
        time = str(raw_input('Enter a time, 24hr >>> '))
        return time

    def getevent():
        event = raw_input('Enter an event >>> ')
        return event

    while True:
        print('\n\nadd, edit, delete, show, menu')
        cmd = raw_input('\n\n>>>>> ')
        

        if cmd == 'add':
            print('Add an event')
            date = getdate()
            if date in user.datebook.date:
                pass
            else:
                user.datebook.adddate(date)
            
            user.datebook.date[date].addevent(gettime(), getevent())


        elif cmd == 'show':
            user.datebook.showdays()
            date = getdate()
            print('\n\n')
            print(user.datebook.date[date].events)


        elif cmd == 'delete':
            user.datebook.showdays()
            which = raw_input('Delete an entry or an entire day? entry/day >> ')
            if which == 'entry':
                user.datebook.date[getdate()].delevent(gettime())
            else:
                user.datebook.deldate(getdate())


        elif cmd == 'edit':
            user.datebook.showdays()
            user.datebook.date[getdate()].editevent(gettime(), getevent())

            
        elif cmd == 'menu':
            user.main_menu(user)

#date_menu()
