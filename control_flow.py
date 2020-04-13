#3 control flow statements: if, for, and while

#if
number = 23
guess = int(input("Enter an integer : "))
#input function -- reusable piece of program. takes user input

if guess == number:
    #new block starts here
    print("Congratulations, you guessed it.")
    print("(but you do not wint any prizes!)")
    #new block ends here
elif guess < number:
    print("No, it is a little higher than that.")
else:
    print("No, it is a little lower than that")
#so it looks like no brackets or semi colons needed around if/else statements in Python

print("Done")
#this last statement is always executed after the if statement is executed

