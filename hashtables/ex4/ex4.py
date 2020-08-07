def has_negatives(a):
    cache = {}

    if len(a) == 0: return a

    for num in a:
        if num < 0:
            if num in cache: continue
            else: cache[num] = []

    for num in a:
        if num > 0:
            if -num in cache:
                cache[-num].append(num)

    return [cache[nums][0] for nums in cache if len(cache[nums]) > 0]


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
