mylist = ["item"]
assert len(mylist) >= 1 #assert method asserts that something is true
print(mylist.pop()) #pop method removes and returns the last item from the list

assert len(mylist) >= 1
#throws an AssertionError, when assert statement fails
