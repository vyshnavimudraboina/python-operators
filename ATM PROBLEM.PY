ICICI_vyshnavi = {
    'name': 'vyshnavi',
    'Adhaar': '456789',
    'Pan': 'dfgh45678jh',
    'ATM PIN': '4444',
    'Balance': 45600
}

remain_Attempts = 3

while remain_Attempts > 0:
    pin = input("Enter your 4 digit pin:")

    if len(pin) == 4:
        if pin in ICICI_vyshnavi['ATM PIN']:
            opt = int(input("\n1.Withdraw \n2.Deposit \n3.Balance \nSelect Your Option:"))

            if opt == 1:
                wd = int(input("Enter amount to be withdrawn:"))
                if wd <= ICICI_vyshnavi['Balance'] and wd % 100 == 0:
                    ICICI_vyshnavi['Balance'] -= wd
                    print(f"You have withdrawn {wd} rs now your total balance is {ICICI_vyshnavi['Balance']}")
                else:
                    print("Can't proceed due to insufficient funds")

            elif opt == 2:
                dep = int(input("Enter amount to deposit:"))
                ICICI_vyshnavi['Balance'] += dep
                print(f"Successfully deposited and your current balance is {ICICI_vyshnavi['Balance']}")

            elif opt == 3:
                print(f"Your total balance is: {ICICI_vyshnavi['Balance']}")

        else:
            remain_Attempts -= 1
            if remain_Attempts > 0:
                print(f"Incorrect pin and you have only {remain_Attempts} attempts")
            else:
                print("Card is blocked")
                break
    else:
        print("Please enter 4 digit pin")
