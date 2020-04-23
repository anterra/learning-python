#on my own: improving io.input program to ignore punctuation, spaces and case
#example to test with: "Rise to vote, sir" should be recognized as palindrome

#plan: scan the text to see if it contains capitals, special characters
#if so, delete the special characters
#and replace capitals with lowercase


#work flow notes:
#first created a tuple of all the forbidden characters
#then discovered the string module! with built in punctuation and alphabet functions :)

#finally realized I should assign text = text.replace(relevant) to change the actual text variable
#(before, I would make the relevant changes, then return(text) and it would return unchanged)

#was trying to think about how to get the position number of a given capital letter within the alphabet
#so I could then replace it with the same letter only lowercase
#but then discovered the function .lower() ! way easier -- just makes the whole thing lowercase, returns same string if already lowercase


def simplify(text):
    import string
    forbidden = string.punctuation
    for character in forbidden:
        text = text.replace(character, "")
    text = text.replace(" ", "") #string.punctuation doesn't include spaces
    text = text.lower()
    return(text)

def reverse(text):
    return text[::-1]

def is_palindrome(text):
    simplified = simplify(text)
    return simplified == reverse(simplified)

something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")

#also note about structure of programs:
#defining the whole set of functions first
#then finally asking user for input dependent on the other functions above
#rather than taking input first and then cascading that input down functions underneath
