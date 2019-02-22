#多型不局限於父子關係，和基底類別與衍生類別觀念一樣
class Animals():
    """這是基底類別"""
    def __init__(self, anima_name):
        self.name = anima_name #紀錄動物名稱
        
    #回傳動物名稱    
    def which(self): 
        return "My pet "+self.name
    
    def action(self): #回傳動物的行為
        return "sleeping"
    
class Dogs(Animals):
    """這是衍生類別"""
    def __init__(self,dog_name):
        super().__init__(dog_name)
    def action(self):
        return "running in the street"
    
class Fish():
    """這是魚的類別"""
    def __init__(self,fish_name):
        self.name=fish_name
    def which(self):
        return self.name
    def action(self):
        return "running in the forest"
def doing(obj):
    print(obj.which(),"is",obj.action())

#呼叫    
animal=Animals("Lala")
doing(animal)

mydog=Dogs("Baa")
doing(mydog)

myfish=Fish("JaJa")
doing(myfish)



    