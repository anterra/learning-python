#operators

#arithmetic
print(3 + 4) #add
print(4 - 3) #substract
print(3 * 5) #multiply
print("la" * 3) #it works on strings!
print(3 ** 4) #exponent
print(13 / 3) #divide
print(13 // 3) #divide and floor -- rounds down to nearest integer
print(13 % 3) #modulo -- gives remainder of the division

#binary
print(2 << 2) #left shift -- shifts the bits of the number to the left by the number of bits specified
# 2 in binary is 10. shifting by 2 bits gives 1000. which is 8
print(11 >> 1) #right shift. see above.
# 11 in binary is 1011. shift right 1 bit gives 101 which is
print(5 & 3) #bit-wise AND (if both true, then true)
print(5 | 3) #bit-wise OR (if one or the other or both true, then true)
print(5 ^ 3) #bit-wise XOR (if either one or the other but not both true, then true)
print(~5) #bit-wise invert -- inverts all binary values (switches 0s to 1s, and 1s to 0s)

#evaluation
print(5 < 3) #less than/great than. returns true or false
print(5 >= 3) #less/greater than or equal to.
print(5 == 3) #equal to
print(5 != 3) #not equal to

#boolean
x = True; y = False; print(not x) #boolean not -- if x is true, returns false. if x is false, returns true.
print(x and y) #boolean and -- returns false if x is false, else it returns evaluation of y
print(x or y) #boolean or -- if x is true, returns true, else returns evaluation of y
#above: evaluates whether x and y // x or y are true
#uses short-circuit evaluation: checks the first one first; if it fails, cancels operation adn returns false without evaluating second term

#shortcut
#for running a math operation on a variable and then assigning the result back to the variable
#example:
a = 2
a = a * 3
#can be written as:
a = 2
a *= 3

#evaluation order -- look up chart if needed
#but basically just use parentheses all the time

