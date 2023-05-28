def find_sum_of_three(nums, target):
   nums.sort()
   for i, n in enumerate(nums[:-2]):
      l = i + 1
      r = len(nums) - 1
      t = target - n
      while l < r:
         cur_s = nums[l] + nums[r]
         if cur_s == t:
            return True
         if cur_s > t:
            r -= 1
            continue
         l += 1

   return False

print(find_sum_of_three([1, 3, 5, 7], 11))