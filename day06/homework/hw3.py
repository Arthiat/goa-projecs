print('password must contain more than 8 char, must Contain A')

password = input("sheiyvanet paroli:")

mcdeloba = 0
while len(password) < 8 or "A" not in password:
    mcdeloba += 1
    if mcdeloba == 3:
        print("tqven agar shegizliat parolis sheyvana")
    password = input("sheiyvanet paroli:")
print("correct")