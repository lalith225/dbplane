def twosums(nums, target):
    res=[]
    for num in range(0, len(nums)):
        for j in range(1, len(nums)):
           if nums[num] + nums[j] == target:
               res=[num,j]
               print(res)
               exit(0)


a = [3,3]
targs = 6
twosums(a, targs)
