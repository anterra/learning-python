#parameters
#parameters: specified within the parentheses in the function definition
#arguments: values for parameters supplied in parentheses when calling the function

def print_max(a, b):
    if a > b:
        print(a, "is maximum")
    elif a == b:
        print(a, "is equal to", b)
    else:
        print(b, "is maximum")

#directly pass literal values
print_max(3, 4)

#pass variables as arguments
x = 5
y = 7
print_max(x, y)