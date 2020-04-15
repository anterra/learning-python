#3 control flow statements: if, for, and while

#if
number = 23
guess = int(input("Enter an integer : "))
#input function -- reusable piece of program. takes user input
#int is a class -- here, it converts our string input into an integer

if guess == number:
    #conditional statements in Python are followed by colon
    #new block indicates arguments
    #no brackets needed
    print("Congratulations, you guessed it.")
    print("(but you do not win any prizes!)")
elif guess < number:
    print("No, it is a little higher than that.")
else:
    print("No, it is a little lower than that")

print("Done")
#this last statement is always executed after the if statement is executed


#while
#allows you to repeatedly execute block of statements as long as a condition is true
#looping statement
#can have optional else clause

number = 23
running = True

while running:
    guess = int(input("Enter an integer: "))

    if guess == number:
        print("Congratulations, you guessed it.")
        #this causes the while loop to stop
        running = False
    elif guess < number:
        print("No, it is a little higher than that.")
    else:
        print("No, it is a little lower than that.")
else:
    print("The while loop is over.")

print("Done")


#for
#looping statement which iterates over a sequence of objects
for i in range(1, 5):
    print(i)
else:
    print("The for loop is over")
#iterates up to the end range, does not include it
#iterates by 1 by default; add 3rd term to range i.e. (range(1, 5, 2)) to iterate by a different nubmer
#generates one number at a time. to get full list:
print(list(range(5)))

#break statement
#used to stop execution of a loop even if condiditon has not become false
#if you break -- any else block is not executed
while True:
    s = input("Enter something: ")
    if s == "quit":
        break
    print("Length of the string is", len(s))
print("Done")


#continue
#used to tell python to skil the rest of the statements in the current loop block and go to next iteration
while True:
    s = input("Enter something: ")
    if s == "quit":
        break
    if len(s) < 3:
        print("Too small")
        continue
    print("Input is of sufficient length")
    #etc.
#should the break statement for quit always come first?
#my inclination would be to define statements first and then lastly give condition that if quit is provided, break..
#testing whether that would be functionally the same:
while True:
    s = input("Enter something: ")
    if len(s) < 3:
        print("Too small")
        continue
    print("Input is of sufficient length")
    if s == "quit":
        break
#seems to run the same! but thinking about it, I agree that its best to check whether we should just quit first
#saves processing power that would be used checking all other conditions/executing any other statements if right away its ready to break.
#short-circuit evaluation!


