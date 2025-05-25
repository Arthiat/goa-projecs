def num(nm):
    num1 = str(nm)[0]
    num2 = str(nm)[1]
    num3 = str(nm)[2]

    res = int(num1) +int(num2)+int(num3)
    return nm % res

print(num(241))


