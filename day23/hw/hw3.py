def arr(x):
    list1 = []
    list2 = []
    for i in x:
        if type(i) ==str:
            list2.append(i)
        else:
            list1.append(i)
    return ' '.join(list2 + list1)