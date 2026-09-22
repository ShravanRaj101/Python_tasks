correct_pin=1234
Deposit_history=[]
Withdrawl_history=[]
balance=5000
pin_attempt=0
ATM_session=True
another_transaction=True
while ATM_session:
    pin=int(input("Enter your pin: "))
    if pin==correct_pin:
        print("Pin verified successfully")
        while another_transaction:
            print("""=====ATM MENU=========
                1.Depost
                2.Withdraw
                3.Balance Inquiry
                4.Deposit History
                5.Witrhdrawl History
                6.Exit
                    """)
            Choice=int(input("Enter your choice:- "))
            if Choice==1:
                amount=float(input("Enter deposit amount: "))
                if amount>0:
                        balance+=amount
                        Deposit_history.append(amount)
                        print("Current Balance",balance)
                else:
                        print("Deposit amount must be greater than zero.")
            elif Choice==2:
                Withdrawl=float(input("Enter withdrawl amount:- "))
                if Withdrawl>0:
                    if Withdrawl<=balance:
                        balance-=Withdrawl
                        Withdrawl_history.append(Withdrawl)
                        print("Withdrawl Successful")
                        print("Current balance:- ",balance)
                    else:
                        print("Insufficient Balance")
                else:
                        print("Withdrawl amount must be greater than zero")
            elif Choice==3:
                print("Available Balance",balance)
            elif Choice==4:
                if len(Deposit_history)==0:
                    print("No deposit has made yet.")
                else:
                    print("deposit History:")
                    for i in Deposit_history:
                        print(i)
            elif Choice==5:
                if len(Withdrawl_history)==0:
                    print("No Withdrawl has made yet.")
                else:
                    print("deposit History:")
                    for i in Withdrawl_history:
                        print(i)
            elif Choice==6:
                print("Thank you") 
                ATM_session=False
                another_transaction=False
                break
            while True:
                again=input("Do you want another transaction? (yes/no): ").lower()
                if again=="no":
                    ATM_session=False
                    another_transaction=False
                    break
                elif again=="yes":
                    another_transaction=True
                    break
                else:
                    print("Invalid Input")
                    print("Please enter only yes or no")
                    
                    
    else:
               print("Incorrect Pin")
               pin_attempt+=1
               if pin_attempt==3:
                   print("Too many incorrect attempts. Please try again later")
                   break
