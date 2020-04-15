#statements in a module can find out the name of their module
#useful for figuring out whether module is being imported

if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("I am being imported from another module")

#executed in command line. result: "this program is being run by itself"
#imported in command line, automatically executes on first import, result: "I am being imported from another module"
