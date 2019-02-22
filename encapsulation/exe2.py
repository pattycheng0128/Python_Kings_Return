class Myschool():

    def __init__(self, name, score):
        self.uname = name
        self.student_score = score
        self.title="Python School"
        
    def msg(self):
        print(self.title,
              "\nHi!", self.uname.title(),",你的成績是", self.student_score, "分")


test = Myschool("kevin", 90)
test.msg()
