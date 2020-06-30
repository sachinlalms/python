# Constructor
# class MySampleClass:
#     def __init__(self):
#         print("Hello!")
# x=MySampleClass()
# y=MySampleClass()

class SecondClass:
    # class Variable
    year=2020
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def add_age(self):
        self.age=self.age+1

    def relocate(self,place):
        self.place=place
    def display(self):
        print("Year:"+str(SecondClass.year+1))
        print("Name:"+self.name)
        print("Age:"+str(self.age))
        print("Place:"+self.place)
    @classmethod
    def add_year(cls):
        SecondClass.year=SecondClass.year+1
    @staticmethod
    def dispaly_welcom():
        print("Welcome")
SecondClass.dispaly_welcom()
z=SecondClass("Sachin",19,"Kannur")
w=SecondClass("Anoop",24,"Iritty")
z.add_age()
w.add_age()
z.display()
w.display()
SecondClass.add_year()
z.add_age()
w.add_age()
z.display()
w.display()
z.relocate("Idukki")
w.relocate("Wayanad")
z.add_age()
w.add_age()
z.display()
w.display()