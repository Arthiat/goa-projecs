def password():
    password = input("password ")
    
    if len(password) < 8:
        print("პაროლი ძალიან მოკლე")
    else:
        print("პაროლი მიღებულია")

password() 