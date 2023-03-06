def inverso(nums):
    inv = []
    for i in range(len(nums) - 1, -1, -1):
        inv.append(nums[i])
    
    print(str(inv).strip('[]'))

nums = [1,2,3,4,5,6,7,8,9]
inverso(nums)