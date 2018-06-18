import math


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def count(mod_list, select):
    sum = 0
    tmp = [0,0,0]
    for i in range(7):
        if select_list[i] != 0:

    return mod_list[select[0]] \
           * (mod_list - [])[select[1]] \
           * mod_list[select[2]]


if __name__ == '__main__':
    mod_list = [0 for i in range(7)]
    for i in range(int(input())):
        mod_list[int(input()) % 7] += 1
    print(mod_list)
    sum = 0
    for i in range(7):
        for j in range(i + 1):
            for k in range(j + 1):
                if (i + j + k) % 7 == 0:
                    select_list = [0 for i in range(7)]
                    select_list[i] += 1
                    select_list[j] += 1
                    select_list[k] += 1
                    sum += count(mod_list, select_list)
                    if (count(mod_list, select_list)):
                        print(select_list)
    print(sum)
