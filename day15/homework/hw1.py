listn = [1,4,3,6,9,11,17,13,26,30]

def pf(listn):
    even_sum = 0
    odd_raodenoba = 0
    for i in listn:
        if i % 2 ==0:
            even_sum += i
        else:
            odd_raodenoba+= 1
    return even_sum, odd_raodenoba

print(pf(listn))