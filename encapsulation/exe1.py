class Myschool():

    def __init__(self, name, score):
        self.uname = name
        self.student_score = score
        
    def msg(self):
        print("Hi!", self.uname.title(),",你的成績是", self.student_score, "分")


test = Myschool("kevin", 90)
test.msg()
