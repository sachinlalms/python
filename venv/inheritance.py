#Inheritance
class BaseClass:
    def set_name(self,name):

        self.name=name



class Subclass(BaseClass):
    def welcome(self):
        print("Welcome")
    def dispaly_name(self):
        print("Name:"+self.name)




y=Subclass()

y.welcome()
y.set_name("Sachin")
y.dispaly_name()