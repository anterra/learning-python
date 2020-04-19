class Person:
    def say_hi(self):
        print("Hello, how are you?")

p = Person()
p.say_hi()

#methods are just like functions, but with an extra self variable
#self variable does not need to be specified when calling method
#last 2 lines can also be written as:
#Person().say_hi()
