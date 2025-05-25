def rem(list):
    result = []
    for i in list:
        if i % 3 == 0:
            result.append(i)
    return result