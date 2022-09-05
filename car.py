class Car:
    def __init__(self,name,model,year,status):
        self.name = name
        self.model = model
        self.year = year
        self.status = status
    
    def drive(self):
        print("The "+self.model+" is driving!")
        
    def stop(self):
        print("The "+self.name+" is stopped")

    def Year(self):
        print("the year is "+str(self.year))
        
class Bike:
    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        
    def Drive(self):
        print("I'm driving the "+self.name+" bike")
        
    def Year(self):
        print("iam using the "+str(self.year)+" version of "+self.model)
        
    def Sound(self,sound):
        print("The sound of the bike is "+sound)