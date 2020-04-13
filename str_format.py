age = 24
name = "Anterra"

print("{0} was {1} years old when she learned python".format(name,age))

name + " is " + str(age) + " years old"
#can also concatenate strings as so but it is ugly and error prone
#also conversion of age to string in first way is automatic via format, this needs explicit coversion

#same output, other options:
print("{} was {} years old when she learned python".format(name, age))
print('{name} was {age} years old when she learned python'.format(name=name, age=age))

#f-strings, quicker
print(f'{name} was {age} years old when she learned python')

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))

# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))

# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

