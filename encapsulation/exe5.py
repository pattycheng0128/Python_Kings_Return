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
        super().__init__("My pet " + dog_name, dog_age)

class Birds(Animals):
    # Animal的衍生類別
    def __init__(self, bird_name, bird_age):
        super().__init__("My pet " + bird_name, bird_age)
    def run(self):
        print(self.name, "is flying")
# 呼叫
mybird = Birds("Lala",5)
mybird.run()
