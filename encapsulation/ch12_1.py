class Banks():
    #定義銀行類別 
    title="Taipei Bank" #定義屬性
    def motto(self): #定義方法
        return "以客為尊" 

    
userbank=Banks() #定義物件userbank
print("銀行是:", userbank.title)
print("銀行理念:", userbank.motto())