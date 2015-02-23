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



user = Date()

def date_menu():
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
        print('\n\nadd, edit, delete, show, cal, quit')
        cmd = raw_input('\n\n>>>>> ')
        

        if cmd == 'add':
            print('Add an event')
            date = getdate()
            if date in user.date:
                pass
            else:
                user.adddate(date)
            
            user.date[date].addevent(gettime(), getevent())


        elif cmd == 'show':
            user.showdays()
            date = getdate()
            print('\n\n')
            print(user.date[date].events)


        elif cmd == 'delete':
            user.showdays()
            which = raw_input('Delete an entry or an entire day? entry/day >> ')
            if which == 'entry':
                user.date[getdate()].delevent(gettime())
            else:
                user.deldate(getdate())


        elif cmd == 'edit':
            user.showdays()
            user.date[getdate()].editevent(gettime(), getevent())

            
        elif cmd == 'quit':
            exit()

#date_menu()
