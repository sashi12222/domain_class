import os
class Bank:
     b_name="SBI"
     def __init__(self,c_name,bal=0.0):
            self.c_name=c_name
            self.bal=bal
     def deposit(self,amt):
         self.bal=self.bal+amt
     def withdraw(self,amt):
         self.bal=self.bal-amt
     def withdraw(self,amt):
         self.bal=self.bal-amt
     def cust_details(self):
       print("customer name:",self.c_name)
       print("Customer_balance",self.bal)

print("****WELOCME TO SBI BANK****")
name=input("Enter customer name:")
b=Bank(name)
while True:
 os.system('cls')
 print("1.deposit\n2.withdraw\n3.cust_details\n4.exit")   
 op=int(input("Enter your option:"))
 if op==1:
      amt=float(input("Enter amount to deposit:"))
      b.deposit(amt)
      print('After Deposite:')
      print("---------------")
      b.cust_details()
 elif op==2:
     amt=float(input("Enter amount to withdraw:"))
     if(b.bal>amt):
       b.withdraw(amt)
     else:
        print("Insufficient balance")
 elif op==3:
    b.cust_details()
 else:
     print("Thank you for banking with us")
      
 