not_in = True
password = "hellow"
while not_in:
    entry = input("Enter a password: ")
    if password == entry:
        not_in = True
        break
    else:
        print("Invalid Password. Try again.")
print ("Password Accepted")