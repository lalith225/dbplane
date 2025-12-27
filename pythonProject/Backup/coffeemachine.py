MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
coffee_state = 'on'
while coffee_state == 'on':
    user_choice = input("What would you like? (espresso/latte/cappuccino):\n")
    if user_choice == 'off':
        coffee_state = 'off'
    if user_choice == 'report':
        for key in resources:
            print(f'{key} : {resources[key]}')
    drink = MENU[user_choice]
    user_dish_ingredients = drink['ingredients']
    for item in user_dish_ingredients:
       if user_dish_ingredients[item] > resources[item]:
           print("sorry bro")




# def check_resource_avail():
#     if user_choice == 'latte':
#         MENU[]
