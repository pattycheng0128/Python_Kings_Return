def build_vip(id,name):
    vip_dict = {"VIP_ID":id,"Name":name}
    return vip_dict

member=build_vip("1","Patty")
print(member)