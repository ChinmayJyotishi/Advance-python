class Student:
    def __init__(self,name,age,sid):
            self.name=name
            self.age=age
            self.sid=sid

    def Printdetails(self):
        return(f'name is {self.name}')
        # print(f'age is {self.age}')
        # print(f'sid is {self.sid}')

s1=Student('chinmay',21,121)
x=s1.Printdetails()
print(x)