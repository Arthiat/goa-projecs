listn = [1,2,3,4,5,6,7]

def f(listn):
    listn2 = []

    for i in listn:
        if i % 2 == 0:
            listn2.append(i)
    return listn2

print(f(listn))
            

