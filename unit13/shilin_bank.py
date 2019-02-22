from unit13 import banks

class Shilin_Banks(banks.Banks):
    def __init__(self, uname):
        self.title = "Taipei Bank-Shilin Branch"

    def bank_title(self):
        return self.title