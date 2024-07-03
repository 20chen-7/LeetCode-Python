'''
sort firstly
TC O(n^2)
SC O(1)
'''
def threeSum(nums):
    nums.sort()#NlogN
    n = len(nums)
    ans = []
    #O(N^2)
    for i in range(n-2):
        #O(N)
        x = nums[i]
        if i > 0 and x == nums[i-1]:
            continue
        if x + nums[i+1]+nums[i+2]>0:
            break
        if x+nums[-1]+nums[-2]< 0:
            continue
        j = i + 1
        k = n - 1
        '''
        template for two sum
        '''
        #O(N)
        while j < k:
            s = nums[i]+nums[j]+nums[k]
            if s == 0:
                ans.append([x, nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j+= 1
                k-=1
                while j < k and nums[k] == nums[k+1]:
                    k-=1
            elif s > 0 :
                k -= 1
            else:
                j += 1
    return ans
        