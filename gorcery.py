print("welcome to our shop")
print('For your surprise we have offers going on:')
print('For your surprise we have offers going on:Buy 2 KGs Sugar and get 50% off and flat 50% off on Wheat flour')
d = {'Rava':70,'Rice':55,'Sugar':50,'Toor dal':150,'Wheat flour':55}
for product,price in d.items():
    print(f"{product}:{price}")

while True:
    item = input('enter the item name')
    if item not in d:
        print('Enter the item name present in our shop and try again.')
        continue
    try:
        quantity=int(input('enter the quantity'))
    except ValueError:
        print('Please enter an integer value.')
        continue

    if item == 'Sugar':
        if quantity >= 2:
            price = (quantity *d[item] )/2
        else:
            price = quantity *d[item]
    elif item =='Wheat flour':
        price=(quantity *d[item] )/2
    else:
        price = quantity *d[item]
    print(f"You have asked for {quantity} Kgs {item}")
    print(f'please pay Rs {price}')





















