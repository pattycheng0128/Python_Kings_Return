import json

fn = "A17000000J-030096-o7m.json"
with open(fn, encoding="utf-8") as fnObj:
    datas = json.load(fnObj)

for data in datas:
    if data["職類別"] == "軟體開發及程式設計師":
        year = data["年度"]
        industry = data["行業別"]
        salary = data["經常性薪資"]
        print("年度:", year, "職類別", industry, "經常性薪資", salary)
        print("----------------------------------------------------")