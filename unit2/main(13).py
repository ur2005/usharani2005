class BankAccount:
  def _init_(self,name,no,abalance):
    self.__account_name=name
    self.__account_no= no
    self.__account_balance=abalance
  def deposit(self,deposit):
    b.BankAccountaccount_balance=b._BankAccount_account_balance+deposit
  def withdraw(self,withdraw):
    b.BankAccountaccount_balance=b._BankAccount_account_balance-withdraw
  def accountbalance(self):
    print('The balance amount is ',b.BankAccount_account_balance)
b=BankAccount("Abitha",123456789,50000)
print("The account holder name:",b.BankAccount_account_name)
print("The account number:",b.BankAccount_account_no)
DA=int(input("Enter deposit amount:"))
b.deposit(DA)
WD=int(input("Enter with drawamount:"))
b.withdraw(WD)
b.accountbalance()