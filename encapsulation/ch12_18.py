class Grandfather():
    """定義祖父類別"""
    def action1(self):
        print("Grandfather")
        
class Father(Grandfather):
    """定義父親類別"""
    def action2(self):
        print("Father")
        
class Uncle(Grandfather):
    """定義叔父類別"""
    def action2(self):
        print("Uncle")
    
class Ivan(Father,Uncle):
    """定義Ivan類別"""
    def action3(self):
        print("Ivan")
#呼叫
ivan=Ivan()
ivan.action3()
ivan.action2()
ivan.action1()

