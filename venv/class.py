class MySampleclass:
    def hello(self,name):
        print("Hello " +name)

x=MySampleclass()

# MySampleclass.hello(x)
name=input("Enter Your Nmae:")
x.hello(name)