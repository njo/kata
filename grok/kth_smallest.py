def k_smallest_number(lists, k):
    # associative array with pointers into list elements
    pointers = [0 for _ in lists]
    count = 0
    ret = None
    while count < k:        # keep adding the smallest until we hit k
        min_i = -1
        latest_min = None
        for i, p in enumerate(pointers):
            if p >= len(lists[i]):
                continue
            num = lists[i][p]
            if latest_min is None or num < latest_min:
                latest_min = num
                min_i = i
        if min_i == -1:
            # no more numbers to add, just bail
            return ret
        ret = latest_min
        pointers[min_i] += 1
        count += 1

    return ret

print(k_smallest_number([[2,6,8],[3,7,10],[5,8,11]], 5))
