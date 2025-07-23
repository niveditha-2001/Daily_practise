import re
def is_valid_email(email):
    return bool(re.match(r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$", email))

def is_valid_card(card):
    return bool(re.match(r"^\d{16}$", card))

def is_valid_gst(gst):
    return bool(re.match(r"^\d{8}[a-zA-Z]{7}$", gst))

def get_valid_input(prompt, validation_function, error_message):
    while True:
        value = input(prompt)
        if validation_function(value):
            return value
        print(error_message)

def main():
    print("Please fill the details to sign in.")

    # Get and validate full name
    full_name = input("Full Name: ")

    # Get delivery address
    print("Delivery address:")
    line1 = input("Line 1: ")
    line2 = input("Line 2: ")
    line3 = input("Line 3: ")

    # Get and validate email
    email = get_valid_input(
        "Email ID: ",
        is_valid_email,
        "Please enter a valid email ID."
    )

    # Get and validate card number
    card = get_valid_input(
        "Card no.: ",
        is_valid_card,
        "Enter a 16-digit card number."
    )

    # Get and validate GST number
    gst = get_valid_input(
        "GST no.: ",
        is_valid_gst,
        "Enter a valid GST number (8 digits followed by 7 alphabets)."
    )
    print("Thank you.")

if __name__ == "__main__":
    main()
