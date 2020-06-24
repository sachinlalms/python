#scop name chech_scop
def check_scop():
# create another function
     def do_local():
         test="local test"
     def do_non_local():
         nonlocal test
         test="non local test"
     def do_global():
         global test
         test="global"
     test="default"
     do_local()
     print("Test value after do local:"+test)
     do_non_local()
     print("Test value after do non local:"+test)
     do_global()
     print("Test value after global:"+test)
check_scop()
print("Test value after main functio:"+test)