def make_icecream(*toppings):
    print("這個冰淇淋的製作材料如下:")
    for topping in toppings:
        print("----",topping )

make_icecream("strawberry","berry","banana")