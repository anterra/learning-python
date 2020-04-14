#default argument values
#for making some parameters optional, w default values
#default values should be immutable.

def say(message, times=3):
    print(message * times)

say("hello")
say("world", 5)

#only need to specify one argument, since the other is default. syntactically not erroneous to leave out 2nd argument
#you can only give default arguments to parameters at the end of a list
#i.e. default parameters cannot precede undefined ones


#keyword arguments
#use the name (keyword) to specify arguments to the function, instead of the parameters position
#advantage: do not need to worry about order of arguments
#advantage: can specify only some arguments, if others have defaults

def func(a, b=5, c=10):
    print("a is", a, "and b is", b, "and c is", c)

func(3,7)
func(25, c=24)
func(c=50, a=100)

