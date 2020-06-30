class MySampleclass:
    def hello(self,n):
        self.name=n
    def print_name(self):
        print(self.name)

x=MySampleclass()
y=MySampleclass()

# MySampleclass.hello(x)
name=input("Enter Your Nmae:")
x.hello(name)
x.print_name()
y.hello("Anoop MR")
y.print_name()