
# coding: utf-8

# In[1]:


## Bank Account Mini project
import math
import random


# In[101]:


class BankAccount():
    def __init__(self, username, accountType, balance=0):
        
        self.username= username ## Username
        self.accountType=accountType  ## checking or saving
        self.balance = balance ## default =0
        self.account = str(random.randint(9999, 99999))
    
    #def Create(self): 
        self.filename = str(self.account) + "_" + self.accountType + "_" +self.username + ".txt"
        f= open(self.filename, "a+")
        f.write("Initial balance: %d\r\n" % self.balance)
        f.close()
        
    def Deposit(self, amount):
        #amount = float(input("Deposit amount: ")
        self.balance += amount
        print(f"Amount Deposit: {amount}")
        fd = open(self.filename, "a+")
        fd.write("Amount Deposited: %d\r\n" % amount)
        fd.write("Balance amount: %d\r\n" % self.balance)         
        fd.close()
                       
    def Withdraw(self, amount):
        #amount = float(input("Withdraw amount: "))
        if self.balance >= amount:
            self.balance -= amount
            print(f"Amount Withdrawn: {amount}")
            
            fw = open(self.filename, "a+")
            fw.write("Amount Withdrawn: %d\r\n" % amount)
            fw.write("Balance amount: %d\r\n" % self.balance)             
            fw.close()
        else: print("Insufficient Balance")
              
    
    def Check_Balance(self):
        print(f"The balance is: {self.balance}")
    
    def account_Type(self):
        print(f"This account is: {self.accountType}")
        
    def accountNumber(self):
        print (f"Account Number is {self.account}")
        
    def Holder_Name(self):
        print(f"this account belongs to {self.username}")
        
    def TransctionHistory(self):
        t = open(self.filename, "r")
        file_lines = t.readlines()
        for line in file_lines:
            print(line)
        t.close()
        #print(tran)
  

 

