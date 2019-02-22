def make_pizza(pizza_size, *toppings):

    print("這個", pizza_size, "吋，材料如下")
    for topping in toppings:
        print("-----", topping)


make_pizza("20", "鳳梨", "番茄", "紅蘿蔔", "海鮮", "魚")
