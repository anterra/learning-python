#scope of variables
#variable names are local to the function
#not related to other variables with the same name outside the function

x = 50

def func(x):
    print("x is", x)
    x = 2 #x in the main block is unaffected by this change. defining a totally separate local variable x
    print("Changed local x to", x)

func(x)
print("x is still", x)

#if not defined inside function, it will reference a variable defined outside the function
#but changes made to the same variable are local only


#global variables
#for assigning a value to a name at top level of program

x = 50
def func2():
    global x

    print("x is", x)
    x = 2
    print("Changed global x to", x)

func2()
print("Value of x is", x)
