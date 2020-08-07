def intersection(arrays):
    cache = {}

    for array in arrays:
        for num in array:
            if num not in cache:
                cache[num] = 0
            
            cache[num] += 1

    return [key for idx, (key, value) in enumerate(cache.items()) if value == len(arrays)]


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
