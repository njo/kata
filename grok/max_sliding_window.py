def find_max_sliding_window(nums, w):
    l, r = 0, w - 1
    cur = nums[l:r+1]
    cur_max = max(cur)
    ret = [cur_max]
    l += 1
    r += 1
    while r < len(nums):
        old_start = cur[0]
        new_end = nums[r]
        cur = nums[l:r+1]

        if cur_max < new_end:
            cur_max = new_end
        elif old_start < cur_max:   # didn't matter
            pass
        else: # old start is >= current max
            cur_max = max(cur)

        ret.append(cur_max)
        r += 1
        l += 1

    return ret

print(find_max_sliding_window([1,2,3,4,5,6,7,8,9,10], 3))
print(find_max_sliding_window([3,3,3,3,3,3,3,3,3,3], 4))
print(find_max_sliding_window([10,6,9,-3,23,-1,34,56,67,-1,-4,-8,-2,9,10,34,67], 2))
print(find_max_sliding_window([9,5,3,1,6,3], 2))
