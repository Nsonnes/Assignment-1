toppings = ''
topping = ''
print('Enter "quit" to exit the program')
while topping != 'quit':
    topping = input('Which topping should be on your pizza? ')
    if topping.lower() == 'quit':
        print('Expect your' + toppings + ' pizza to be delivered in 10 minutes')
    else:
        toppings = toppings + ' ' + topping
        print('Excellent choice! Your pizza now contains ' + toppings)


