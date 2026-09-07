
def greetings(first_name):
    first_name ="Khalilah"

#print(first_name)

#    print(first_name)
#          ^^^^^^^^^^
#NameError: name 'first_name' is not defined

def greet(name):
    message = f"Bonjour, {name}!"
    return message

my_name = greet("Khalilah")
print(my_name)