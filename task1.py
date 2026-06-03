class BackAccount:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number=account_number
        self.balance=balance
        self.owner_name=owner_name
        self.date_opened=date_opened
        def deposit(self,amount):
            print(f"{self.owner_name} deposit {amount}")
            self.balance=amount+self.balance

            def check_balance(self,balance):
                    print(f"{self.owner_name} Your balance is{self.balance}")

                    def withdrawal(self,withdraw):
                         self.balance=self.balance-amount
                         if amount<=self.balance:
                              print(f"{self.owner_name} withdrew{amount}.New balance is{self.balance}")
                         else:
                              print(f"{self.owner_name},insufficient funds")

                              def get_details(self):
                                   print(f"customer's name:{self.owners_name},Account Number:{self.account_number},Balance:{self.balance}")
                                        
                                   
                                        
                                   
                                   
                                   def close_account(self):
                                        print(f"{self.owner} account has been closed")

                          account1= BackAccount(4567,45000,"Sally",12-3-2026) 
                         print(account1.account_number)
                         print(account1.balance)
                         print(account1.owner_name)
                         print(account1.date_opened)
                         account1.deposit(5000)
                         account1.checkbalance()
                         account1.withdraw(10000)
                         account1.get_details()
                         account1.close_account()

                         account2=BackAccount(5460,50000,"Mary",3-4-2026)
                         print(account2.account_number)
                    
                         print(account2.balance)
                         print(account2.owner_name)
                         print(account2.date_opened)
                         account2.deposit(5000)
                         account2.checkbalance()
                         account2.withdraw(10000)
                         account2.get_details()
                         account2.close_account()


                         
                                 




                    
                         

                    
        



        