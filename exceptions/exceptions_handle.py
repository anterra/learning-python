try:
    text = input("Enter something --> ")
    #if the text you enter is [ctrl]-d = EOF, [ctrl]-c = cancel
except EOFError:
    print("Why did you do an EOF on me?")
except KeyboardInterrupt:
    print("You cancelled the operation.")
else:
    print("You entered {}".format(text))

