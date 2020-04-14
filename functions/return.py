#return statement
#the return statement is used to break out of a function
#can optionally return a value as well

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return "the numbers are equal"
    else:
        return y

print(maximum(2, 3))

#a return statement without a value is equivalent to return None
#None is a special type in Python that represents nothingness

#note for this example: there's actually a 'max' function built-in to python that finds maximum, so use that whenever
