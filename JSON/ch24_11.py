import json

fn = "A17000000J-030100-8gL.json"
with open(fn, encoding='utf8') as fnObj:
    getDatas = json.load(fnObj)  # 讀取json資料

for data in getDatas:
    if data["職類別"] == "軟體開發及程式設計師":
        year = data["年度"]
        industry = data["職類別"]
        salary = data["經常性薪資"]
        print("年度:", year, "職類別:", industry, "經常性薪資:", salary)
        print("------------------------------------------------")

