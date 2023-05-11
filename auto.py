import datetime


class Auto:
    def __init__(self, controller):
        self.controller = controller
    
    def normilizeTime(self, time):
        return datetime.datetime.combine(datetime.date.today(), datetime.time(hour=int(time.split(':')[0]), minute=int(time.split(':')[1])))
    
    def createTime(self):
        return datetime.datetime.combine(datetime.date.today(), datetime.time(hour=int(datetime.datetime.strftime(datetime.datetime.now(), '%H')), minute=int(datetime.datetime.strftime(datetime.datetime.now(), '%M'))))
    
    def check(self, settings):
        while True:
            if datetime.date.weekday() == 0:
                settings = settings['mon']
            elif datetime.date.weekday() == 1:
                settings = settings['tue']
            elif datetime.date.weekday() == 2:
                settings = settings['wed']
            elif datetime.date.weekday() == 3:
                settings = settings['thu']
            elif datetime.date.weekday() == 4:
                settings = settings['fri']
            elif datetime.date.weekday() == 5:
                continue
            elif datetime.date.weekday() == 6:
                continue
            
            for i in settings:
                for j in i:
                    if self.normilizeTime(j) == self.createTime():
                        self.controller.turnOn('pin1')
                    else:
                        self.controller.turnOff('pin1')
                        