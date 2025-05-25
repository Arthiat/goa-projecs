listn = [1,2,3,4,5,6]
def manual_reverse(lst):
    lstn = []
    for i in lst:
        lstn.insert(0, i)
    
    return lstn
print(manual_reverse(listn))