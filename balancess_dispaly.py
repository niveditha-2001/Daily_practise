def main():
    database = {
        100: {'name': 'Deepthi', 'Pin': 1234, 'Net balance': 0},
        101: {'name': 'Eva', 'Pin': 2345, 'Net balance': 100000},
        102: {'name': 'Raghavendra', 'Pin': 3456, 'Net balance': 110000},
        103: {'name': 'Sthuthi', 'Pin': 4567, 'Net balance': 85000},
        104: {'name': 'Sujay', 'Pin': 5678, 'Net balance': 50500}
    }
    Account_num=int(input('Please enter your Account no.:'))
    if Account_num not in database:
        print('Entering wrong account no. Please try again.\nPlease visit our bank and create an account.')
        return
    pin=int(input('Please enter the 4 digit pin:'))
    if database[Account_num]['Pin']!=pin:
        print('Sorry Invalid Pin.')
    else:
        customer = database[Account_num]
        print(f"Hi {customer['name']}")
        print(f'Your net balance is:{customer['Net balance']}')
main()