#Inheritance
class BaseClass:
    def __init__(self):
        print("Base Init")
    def set_name(self,name):
        self.name=name
        print("Base Class Set_name")


class Subclass(BaseClass):
    def __init__(self):
        super().__init__()
        print("Sub class init") #constuctor over_riding

    def set_name(self,name):
        self.name=name         #method over
        super().set_name(name)
        print("Sub Class Set_name")
    def welcome(self):
        print("Welcome")

    def dispaly_name(self):
        print("Name:"+self.name)




y=Subclass()

y.welcome()
y.set_name("Sachin")
y.dispaly_name()