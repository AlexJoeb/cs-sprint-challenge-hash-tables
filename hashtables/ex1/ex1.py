def get_indices_of_item_weights(weights, length, limit):
    cache = {} # Init a cache.

    # Iterate over all weights and add them to cache; value intialized to index.
    for idx in range(length):
        cache[weights[idx]] = idx

    for idx in range(length):
        key = limit - weights[idx]
        if key in cache:
            return (
                idx if idx > cache[key] else cache[key],
                idx if idx < cache[key] else cache[key]
            )

    return None

get_indices_of_item_weights([1, 3, 4, 6, 7, 8], 6, 14)