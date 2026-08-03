ICICI_vyshnavi = {
    'name': 'vyshnavi',
    'Adhaar': '456789',
    'Pan': 'dfgh45678jh',
    'ATM PIN': '4444',
    'Balance': 5000,
    'TH':[]} 


remain_Attempts = 3

while remain_Attempts > 0:
    pin = input("Enter your 4 digit pin:")

    if len(pin) == 4:
        if pin in ICICI_vyshnavi['ATM PIN']:
            opt = int(input("\n1.Withdraw \n2.Deposit \n3.Balance \n4.Transaction History \n5.pin change \nSelect Your Option:"))

            if opt == 1:
                wd = int(input("Enter amount to be withdrawn:"))
                if wd <= ICICI_vyshnavi['Balance'] and wd % 100 == 0:
                    ICICI_vyshnavi['Balance'] -= wd
                    ICICI_vyshnavi['TH'].append(f'Withdraw : {wd}')
                    print(f"You have withdrawn {wd} rs now your total balance is {ICICI_vyshnavi['Balance']}")
                    user_1 = int(input('enter \n1.home page \n2.exit: '))
                    if user_1 == 1:
                        print('home page')
                    else:
                        print('thank you for visiting')
                    
                else:
                    print("Can't proceed due to insufficient funds")

            elif opt == 2:
                dep = int(input("Enter amount to deposit:"))
                if dep % 100 == 0:
                   ICICI_vyshnavi['Balance'] += dep
                   ICICI_vyshnavi['TH'].append(f'Deposite :{dep}')
                   print(f" you have deposite {dep} and the total balance is {ICICI_vyshnavi['Balance']} ")
                   
                   
                else:
                    print('change can not be deposite')
                    break

            elif opt == 3:
                print(f"Your total balance is: {ICICI_vyshnavi['Balance']}")
                ICICI_vyshnavi['TH'].append(f"your balance is {ICICI_vyshnavi['Balance']}")
                
            elif opt == 4:
                if len(ICICI_vyshnavi['TH'])==0:
                    print('no transaction found:')
                else:
                    print('Transaction History')
                    for i in ICICI_vyshnavi['TH']:
                        if 'Withdraw' in i or 'Deposite' in i:
                            print(i)

            elif opt == 5:
                  old_pin = input('enter your old PIN: ')
                  if old_pin ==ICICI_vyshnavi['ATM PIN']:
                     new_pin = input('enter your new 4 digit PIN: ')
                     if len(new_pin) == 4:
                        ICICI_vyshnavi['ATM PIN'] = new_pin
                        print('PIN changed successfully')
                     else:
                         print('please enter 4 digit PIN:')
                  else:
                     print('incorrect old PIN')
                      
                        
                

        else:
            remain_Attempts -= 1
            if remain_Attempts > 0:
                print(f"Incorrect pin and you have only {remain_Attempts} attempts")
            else:
                print("Card is blocked")
                break
    
           
    else:
        
               
        print("Please enter 4 digit pin")




OUTPUT



Enter your 4 digit pin:4444

1.Withdraw 
2.Deposit 
3.Balance 
4.Transaction History 
5.pin change 
Select Your Option:1
Enter amount to be withdrawn:1000
You have withdrawn 1000 rs now your total balance is 4000
enter 
1.home page 
2.exit: 1
home page
Enter your 4 digit pin:4444

1.Withdraw 
2.Deposit 
3.Balance 
4.Transaction History 
5.pin change 
Select Your Option:2
Enter amount to deposit:2000
 you have deposite 2000 and the total balance is 6000 
Enter your 4 digit pin:4444

1.Withdraw 
2.Deposit 
3.Balance 
4.Transaction History 
5.pin change 
Select Your Option:3
Your total balance is: 6000
Enter your 4 digit pin:4444

1.Withdraw 
2.Deposit 
3.Balance 
4.Transaction History 
5.pin change 
Select Your Option:4
Transaction History
Withdraw : 1000
Deposite :2000
Enter your 4 digit pin:4444

1.Withdraw 
2.Deposit 
3.Balance 
4.Transaction History 
5.pin change 
Select Your Option:5
enter your old PIN: 4444
enter your new 4 digit PIN: 7777
PIN changed successfully
Enter your 4 digit pin:4444
Incorrect pin and you have only 2 attempts
Enter your 4 digit pin:7777

        
