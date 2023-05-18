'''
https://leetcode.com/problems/two-sum/
3. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''    

def two_sum_Weston_iterative(nums, target):
  for i in range(len(nums)):
    for j in range(len(nums)):
      # continue skips one single iteration of a loop
      if i == j:
        continue
      elif nums[i] + nums[j] == target:
        return[i, j]

# enumerate breakdown
my_fruit = ["mango", "banana", "berry", "watermelon"]
enum_fruit = enumerate(my_fruit)
for thing in enum_fruit:
  print(thing)
  i, fruit = thing
  print(i, fruit)

def two_sum_Weston_hash(nums, target):
  hash_table = {}
  for i, num in enumerate(nums):
    # target - num = number to match with
    match_number = target - num
    if match_number not in hash_table:
      hash_table[num] = i
    else:
      return [hash_table[match_number], i]

def two_sum(nums, target):
  hash_table = {}
  for num in range(len(nums)):
    hash_table[num] = nums[num]
    # print(f" num: {num} hash: {hash_table[num]}")
    second_num = num - 1
    search = True
    while second_num >= 0 and search:
      if hash_table[num] + hash_table[second_num] == target:
        print(f"num_one: {hash_table[num]} + second_num: {hash_table[second_num]} == {target}, return {num} and {second_num}")
        search = False
        return [num, second_num]
      else: 
        second_num -= 1

def two_sum_alt(nums, target):
  hash_table = {}
  for num in range(len(nums)):
    second_num = target - nums[num]
    if second_num in hash_table:
      return [hash_table[second_num], num]
    hash_table[nums[num]] = num

def two_sum_alt_alt(nums, target):
  hash_table = {}
  for i, num in enumerate(nums):
    second_num = target - num
    if second_num in hash_table:
      return [hash_table[second_num],i]
    hash_table[num] = i

print(two_sum_Weston_iterative([2,7,11,15], 9))
print(two_sum_Weston_hash([2,7,11,15], 9))
print(two_sum([2,7,11,15], 9))
print(two_sum_alt([2,7,11,15], 9))
print(two_sum_alt_alt([2,7,11,15],9))