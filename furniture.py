def main():

    products = {
        "pdcR012": {"type": "Shelf", "price": 0, "quantity": 0, "location": None},
        "pdcc01": {"type": "Chair", "price": 1500, "quantity": 10, "location": "B1R1C2"},
        "pdcs11": {"type": "Sofa", "price": 50000, "quantity": 5, "location": None},
        "pdct01": {"type": "Table", "price": 20000, "quantity": 3, "location": None}
    }


    product_code = input("Please enter the product code: ").strip()
    if product_code not in products:
        print("Please enter a valid product code.")
        return

    product = products[product_code]
    if product["quantity"] == 0:
        print(f"Product Type: {product['type']}")
        print("Sorry! Out of stock")
        return
    print(f"Product Type: {product['type']}")

    if product["type"] == "Sofa" or product["type"] == "Table":
        total_price = product["price"] + 600
        print(f"Product Price: {product['price']} + 600/- Rs. Delivery charge.")
        print(f"Please pay Rs. {total_price}")
        print("The product will be delivered to your home.")
    else:
        print(f"Price: {product['price']}")
        print(f"You can collect the product in the ground floor, Bay: {product['location'][1]} Row: {product['location'][3]} Column: {product['location'][5]}")
main()