def containsNearbyDuplicate(nums, k) -> bool:
    dict_num = {}
    small_g = k + 1
    for i, v in enumerate(nums):
        if v not in dict_num.keys():
            dict_num[v] = [i]
        else:
            for a in dict_num[v]:
                if small_g > abs(i - a):
                    small_g = abs(i - a)
            dict_num[v].append(i)

    if small_g <= k:
        return True
    else:
        return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate(nums, k))
print("11")
print('2222')
