def make_icecream(*toppings):
    print("列出冰淇淋的配料")
    for topping in toppings:
        print("-----", topping)


def make_drink(size, drink):
    print("所點飲料如下:")
    print("-----", size.title())
    print("-----", drink.title())