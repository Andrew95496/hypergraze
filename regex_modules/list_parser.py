def split_LINK(array):
    array2 = []
    for i in array:
        x = i.split("//", 1)
        if len(x) == 2:
            array2.append(x[1])
    return array2[0:6]


def split_ATTR(array):
    array2 = []
    for i in array:
        x = i.split("=", 1)
        array2.append(x[1])
    return array2[0:6]