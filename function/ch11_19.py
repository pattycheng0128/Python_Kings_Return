def product_msg(customers):
    str1 = "親愛的:"
    str2 = "本公司將於XXX舉行"
    str3 = "總經理 敬上"
    for customer in customers:
        msg = str1 + customer + str2 + str3
        print(msg)

members = ["A", "B", "C"]
product_msg(members)