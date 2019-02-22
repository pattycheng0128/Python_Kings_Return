class Grandfather():
    """定義祖父類別"""

    def action1(self):
        print("Grandfather")


class Father(Grandfather):
    """定義父親類別"""

    def action4(self):
        print("Father")


class Uncle(Grandfather):
    """定義叔父類別"""

    def action3(self):
        print("Uncle")

class Aunt(Grandfather):
    """定義姑媽類別"""

    def action2(self):
        print("Aunt")


class Ivan(Father, Uncle, Aunt):
    """定義Ivan類別"""

    def action5(self):
        print("Ivan")


# 呼叫
ivan = Ivan()
ivan.action5() #Ivan
ivan.action4() #Ivan→Father
ivan.action3() #Ivan→Father→Uncle
ivan.action2()  #Ivan→Father→Uncle→Aunt
ivan.action1() #Ivan→Father→Uncle→Aunt→Grandfather

