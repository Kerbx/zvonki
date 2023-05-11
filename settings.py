import pickle


class Settings:
    def __init__(self):
        self.filename = 'setting.pickle'
        self.time = {}
        
        self.loadSettings()
        
    def loadSettings(self):
        with open(self.filename, 'rb') as file:
            self.time = pickle.load(file)
    
    def saveSettings(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.time, file)
        