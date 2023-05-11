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
            if datetime.date.weekday(datetime.date.today()) == 0:
                setting = settings['mon']
            elif datetime.date.weekday(datetime.date.today()) == 1:
                setting = settings['tue']
            elif datetime.date.weekday(datetime.date.today()) == 2:
                setting = settings['wed']
            elif datetime.date.weekday(datetime.date.today()) == 3:
                setting = settings['thu']
            elif datetime.date.weekday(datetime.date.today()) == 4:
                setting = settings['fri']
            elif datetime.date.weekday(datetime.date.today()) == 5:
                continue
            elif datetime.date.weekday(datetime.date.today()) == 6:
                continue
            
            for i in setting:
                for j in i:
                    if j:
                        if self.normilizeTime(j) == self.createTime():
                            self.controller.turnOn('pin1')
                            break
                        else:
                            self.controller.turnOff('pin1')
                        