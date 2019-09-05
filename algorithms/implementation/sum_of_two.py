

def sum_of_two(arr, target):
    hash_set = set()
    res = []
    for e in arr:
        if (target - e) in hash_set:
            res.append([e, target - e])
        else:
            hash_set.add(e)
    print(res)

if __name__ == "__main__":
    sum_of_two([2, 1, 8, 4, 7, 3], 3)
    sum_of_two([2, 1, 8, 4, 7, 3], 21)