def main():
    payable_amount = 1500
    print("Welcome to online shopping.")
    print("your cart is not empty.")
    print(f"You have to pay Rs. {payable_amount}/-")
    coupon = input("Do you have coupon? type y or n: ")

    if coupon == 'y':
        coupon_code = input("Please enter the coupon code: ")
        if coupon_code == 'CDEC01':
            payable_amount -= 500
            print(f"successfully applied the coupon code. Please pay {payable_amount}/-")
        elif coupon_code == 'ONEJAN02':
            payable_amount /= 2
            print(f"successfully applied the coupon code. Please pay {payable_amount}/-")
        elif coupon_code == '2234150':
            print("successfully applied the coupon code.")
            print(f"Congratulations! You got 1000 loyalty points for shopping with us.Please pay {1500}/-")

        else:
            print("Invalid coupon code. Please enter a valid coupon.")
            print(f"Please pay {1500}/-")
    else:
        print(f"Please pay Rs. {1500}/-")
main()