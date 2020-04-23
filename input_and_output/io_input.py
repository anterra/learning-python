def reverse(text):
    return text[::-1] #slicing function. arguments are start stop step count. -1 returns text in reverse

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")

