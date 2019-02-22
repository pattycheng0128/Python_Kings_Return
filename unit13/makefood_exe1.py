def make_icecream(*toppings):
    print("冰淇淋所加的材料:")
    for topping in toppings:
        print(topping)


def make_drink(size, drink):
    print("所點飲料如下:")
    print(size.title())
    print(drink.title())


def make_noodle(noodle_type, *toppings):
    print("%s的配料如下:" % noodle_type)
    for topping in toppings:
        print(topping)