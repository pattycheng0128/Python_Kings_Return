class Animals():
    
    # 這是基底類別
    def __init__(self, animal_name, animal_age):
        self.name = animal_name
        self.age = animal_age
    
    def run(self):
        print(self.name, "is runnung")
        

class Dogs(Animals):

        # Animal的衍生類別
    def __init__(self, dog_name, dog_age):
        super().__init__("My pet "+ dog_name, dog_age)


# 呼叫        
mycat = Animals("Lucy", 10)
print(mycat.name, "年齡:", mycat.age, "歲")
mycat.run()
print("-----------------------")
mydog = Dogs("Lala", 5)
print(mydog.name, "年齡", mydog.age, "歲")
mycat.run()        
