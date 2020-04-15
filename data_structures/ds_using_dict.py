#"ab" is short for addressbook

ab = {
    "Swaroop": "swaroop@swaroopch.com",
    "Larry": "larry@wall.org",
    "Matsumoto": "matz@ruby-lang.org",
    "Spammer": "spammer@hotmail.com"
}

print("Swaroop's address is", ab["Swaroop"])

#deleting a key-value pair
del ab["Spammer"]

print("\nThere are {} contacts in the address-book\n".format(len(ab)))
#\n is a line break, added to separate sections

for name, address in ab.items():
    print("Contact {} at {}".format(name, address))
    #retrieve each tuple pair and assign it to the variables name, address respectively

#adding a key-value pair
ab["Guido"] = "guido@python.org"

if "Guido" in ab:
    print("\nGuido's address is", ab["Guido"])
