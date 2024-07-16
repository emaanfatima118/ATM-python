import time
print("""WELCOME TO HBL 
INSERT YOUR CARD IN MACHINE""")
time.sleep(3)
pw = 1234
pin = int(input("Enter your pin: "))
balance = 10000
if pin == pw:
  while True:

        print("""
        1: balance
        2: withdraw
        3: deposit
        4: exit
        """)
        try:
            option = int(input("Please enter your choice (1-4): "))
        except:
            print("Please enter valid option")
        if option == 1:
            print(f"Current balance: {balance}")
        if option == 2:
            w_amount = int(input("Please enter withdrawal amount: "))
            balance = balance-w_amount
            print(f"{w_amount} is debited from your account")
            print(f"Updated balance {balance}")
        if option == 3:
            d_amount = int(input("Please enter deposit amount: "))
            balance = balance+d_amount
            print(f"{d_amount} is credited from your account")
            print(f"Updated balance {balance}")
        if option == 4:
            print("Thankyou for coming!")
            break
else:
    print("Wrong pin! Try again.")
