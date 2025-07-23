from datetime import datetime, timedelta
today_date = datetime.strptime("12/01/22", "%m/%d/%y")
products = {
    1: {"name": "Soap", "expiry_date": today_date + timedelta(days=30)},
    2: {"name": "Shampoo", "expiry_date": today_date - timedelta(days=5)},
    3: {"name": "Tooth paste", "expiry_date": today_date - timedelta(days=10)},
    4: {"name": "Ready juice", "expiry_date": today_date + timedelta(days=20)},
    5: {"name": "Chips", "expiry_date": today_date + timedelta(days=15)},
}
def check_expiry(product_code):
    if product_code in products:
        product = products[product_code]
        product_name = product["name"]
        expiry_date = product["expiry_date"]
        if expiry_date < today_date:
            return f"Product name: {product_name}\nExpired"
        else:
            return f"Product name: {product_name}\nGood to sale"
    else:
        return "Enter the existing product code."

# Main program loop
print("Welcome to ABC super market's inspection portal")
print(f"Today's Date is:{today_date.strftime('%m/%d/%y')}")
while True:
    try:
        product_code = int(input("Enter the product code: "))
        result = check_expiry(product_code)
        print(result)
        if result == "Enter the existing product code.":
            break
    except ValueError:
        print("Invalid input. Please enter a valid product code.")
        break