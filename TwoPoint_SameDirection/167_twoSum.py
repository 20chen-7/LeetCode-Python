'''
two point for the same direction
=> numbers array is sorted
'''
def twoSum(numbers, target):
    l = 0
    r = len(numbers)-1
    while l < r:
        s = numbers[l]+numbers[r]
        if s == target:
            break
        
        if s > target:
            r -= 1
        else:
            l += 1
    return [l+1, r+1]
    