listn = [1,23,165,2,3,92,10,34,911]
def pf(listn, gamyopi):
    result = []
    for num in listn:
        if num % gamyopi == 0:
            result.append(num)
    
    return result

print(pf(listn, 3))