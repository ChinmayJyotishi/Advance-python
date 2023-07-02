class BankOperation:
    Bankname="Indian express bank"
    Branch="Patia"
    def __init__(self,username,pan,AdharNum,address):
        self.name=username
        self.pan=pan
        self.adhar=AdharNum
        self.address=address
        self.balanace=0.0
        print(f"Hello {username} Congratulations account creation successfully")
    
    def Deposite(self,amount):
        self.balanace=self.balanace+amount
        print(f'{amount} is dposited in your account\n')
    def Withdraw(self,Wamount):
        if amount<self.balanace:
                 self.balanace=self.balanace-Wamount
                 print(f'{Wamount} is withdrwal successfully\n')
        else:
            print("Insufficient balance")
   
    def Ministatement(self):
        print(f'Your total balance is {self.balanace}')

    
print(f'Welcome to {BankOperation.Bankname},{BankOperation.Branch} Branch')
name=input("Enter Your Name: ")
PanNum=input("Enter Your Pan Number: ")
Adhar=input("Enter Your Adhar Number: ")
address=input("Enter Your Address: ")

BankObj=BankOperation(name,PanNum,Adhar,address)

while True:
    print("choose one option to perform operation: ")
    print("1:Deposite\n2:withdraw\n3:ministatement\n4:Exit ")
    option=int(input())

    if option==1:
        amount=float(input("Enter the amount to deposite: "))
        BankObj.Deposite(amount)
    elif option==2:
        Wamount=int(input("Enter the amount to withdraw: "))
        BankObj.Withdraw(Wamount)
    elif option==3:
        BankObj.Ministatement()
    elif option==4:
        print("Thank You For using Indian Express Bank")
        break
    else:
        print("Invaild Instance Provided\n")
        