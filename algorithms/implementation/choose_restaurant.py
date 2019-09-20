def findRestaurant(list1, list2):
    res = {}
    for i in list1:
        if i in list2:
            res[i] = sum([list1.index(i), list2.index(i)])

    min_v = min(res.values())
    r = [k for k, v in res.items() if v == min_v]
    return r