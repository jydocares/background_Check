#Inputting user information
argument = True
container = []
while argument:
    x = input("Enter first name:")
    y = input("Enter last name:")
    z = input("Enter email:")
    info = {'first name': x, 'last name': y, 'email': z}

#Generating the random password
    import string
    import random
    (string.ascii_letters + string.digits,5)
    ink = (''.join(random.sample((string.ascii_letters + string.digits)*5,5)))
    password = ((x[0:2] + y[-2:]) + ink)

#Total output
    password_loop = True
    while password_loop:
#Get user details
        print(info)

#Show generated password
        print("Your password is : "+ str(password))

#Ask if he would like to continue
        password_like = input("Do you like the generated password? \n If Yes, Enter 'Yes' \n If No, Enter 'No' and supply:")
        if password_like == "yes":
            print(password)
            break

#Password_like == "no"
        else:
            password = input("Enter password longer than 7 character:")

    #password length loop
        if len(password) >=7:
            print(password)
            break

        while True:
            if len(password) < 7:
                print("Your password is lower than seven(7)")
                password = input("Enter your password to be seven(7) characters and above: ")

            else:
                print("Password accepted")
                break
    count = 1
    new_user = input("Enter new user \n ").upper()
    if new_user == "NO":
        argument = False
        for details in container:
            print(details)

    else:
        argument = True