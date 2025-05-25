def most_common_type(lst):
    type = {}
    for i in lst:
        t = type(i)
        type[t] = type.get(t, 0) + 1
    most_common = max(type, key=type.get)
    return most_common.__name__