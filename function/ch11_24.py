def make_icecream(icecream_type, *toppings):
    print("這個", icecream_type, "冰淇淋所加的材料如下")
    for topping in toppings:
        print("----",topping)

make_icecream("芒果","草莓醬","香蕉片")