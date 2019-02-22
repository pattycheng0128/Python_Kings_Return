def guest_info(firstname, middlename, lastname , gender):
    if gender == "M":
        welcome = firstname + " " + middlename + " " + lastname + "先生歡迎你"
    else:
        welcome = firstname + " " + middlename + " " + lastname + "小姐歡迎你"
    return welcome
info1 = guest_info ("Pei","Ting","Cheng","F")
print(info1)