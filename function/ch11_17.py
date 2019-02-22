def build_vip(id, name, tel=""):
    vip_dict = {"VIP_ID":id,"Name":name}
    # 如果有輸入電話號碼，將內容加到字典裡面
    if tel:
        vip_dict["Tel"] = tel
    return vip_dict

member1 = build_vip("1","Patty")
member2 = build_vip("2","JJ","2233-1222")
print(member1)
print(member2)