#functions = a block of code which is executed only when it is clled!!

def hello():
    print("hello!")
    print("have a nice day!")
hello()

def hello(first_name,last_name,age):
    print("hello "+first_name+" "+last_name)
    print("your age is "+str(age)+" years old")
     print("have a nice day!")
hello("xiang","tzu",25)
hello("jack")

#****an important feature of functions
# is we can send information to our function(it could be str,variable,collection.....etc anything!!) ****
#                                  the information we pass is called an **argument**
#**another way of writting code**
def hello(first_name,last_name,age):
    full_name = first_name + last_name
    print("hello "+full_name)
    age = str(age)
    print("your age is "+age+" years old")
    print("have a nice day")
hello("xiang","tzu",25)
