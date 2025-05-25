def arr (x,y):
    if x >y:
        return x/y
    if y>x:
        return y/x
    if x == 0 or y==0:
        return "ZeroDivissionError"