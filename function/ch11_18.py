def build_vip(id, name, tel=""):
    vip_dict={"vip_id":id, "Name":name}
    if tel:
        vip_dict["Tel"] = tel
    return vip_dict

while True:
    print("VIP資訊")
    idnum = input("請輸入id:")
    name = input("請輸入姓名:")
    tel = input("請輸入電話:")
    member = build_vip(idnum, name, tel)
    print(member)
    repeat = input("是否繼續(y/n):")
    if repeat == "n":
        break
print("歡迎下次再使用")