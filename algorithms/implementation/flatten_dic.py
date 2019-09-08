def flatten_dictionnary(d, new_dic, key=""):
    for k, v in d.items():
        if type(v) is dict:
            if not key:
                key = k 
            else:
                key += k
            flatten_dictionnary(d[k], new_dic, key + '_' )
            key = ""
        elif type(v) is list:
            for i, e in enumerate(v):
                new_dic[key + k + "_" + str(i)] = e
        else:
            if key:
                new_dic[key + k] = v
            else:
                new_dic[k] = v

    return new_dic


if __name__ == "__main__":
    d = {
        "a": 1,
        "c": {"a": 2},
        "b": {"t": 5, "y": 10, 'f':{'a':1}},
        "e": [1, 2],
        "z": {"k": 2, "xx": [3, 4]},
        "w": {"a": {"c": [5, 6], "d": 4}},
    }
    new_dic = flatten_dictionnary(d, {}, "")
    print("New dic:", new_dic)
