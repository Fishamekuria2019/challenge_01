"""This is a basic ATM Application.

This is a command line application that mimics the actions of an ATM.

Example:
    $ python app.py
"""

accounts = [
    {
    "pin": 123456,
    "balance" : 1436.19},
    {
    "pin" : 246802,
    "balance": 3571.87},
    {
    "pin": 135791,
    "balance" : 543.79},
    {
    "pin" : 123987,
    "balance": 25.89},
    {
    "pin" : 269731,
    "balance": 3258.42}
]


# Create the `login` function for the ATM application.
balance = 0

def login(pin):
    for x in accounts:
        # x = {
        #     "pin" : 269731,
        #     "balance": 3258.42
        # }
        if pin==x["pin"]:

            # continue
            return x["balance"]
    print("Wrong pin number, please try again")
    return False


def read_pin():
    try:
        pin = int(input("Please enter your pin number"))
        if pin:
            balance = login(pin)
            return balance

    except:
        print("Error please enter digits only")
    read_pin()
    


def check_balance():
    return balance  