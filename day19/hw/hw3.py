def negpos(list1, list2):
    tog= list1+ list2
    posnum = 0
    negnum = 0
    for i in tog:
        if i <0:
            negnum += 1
    else:
        posnum +=1

    return posnum, negnum