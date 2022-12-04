def isHappy(n: int) -> bool:
    n_exit = set()
    n_exit.add(n)
    while True:
        n_str = str(n)
        sum_n = 0
        for i in n_str:
            sum_n += int(i)**2
        if sum_n == 1:
            return True
        if sum_n in n_exit:
            return False
        n = sum_n
        n_exit.add(n)


print(isHappy(2))









