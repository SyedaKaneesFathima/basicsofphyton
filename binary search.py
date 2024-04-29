nums=list(map(int,input().split())
nums = sorted(nums)
target =int(input())
left = 0 
right = len(nums) - 1 
found = False
while left <= right:
    mid = (left + right) // 2 
    if nums[mid] == target:
        found = True
        break 
    elif nums[mid] > target:
        right = mid - 1 
    else:
        left = mid + 1 
if found == True:
    print("Found")
else:
    print("Not found")
 
