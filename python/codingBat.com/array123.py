def array123(nums):
    for item in range(len(nums)-2):
        if nums[item] == 1 and nums[item+1] == 2 and nums[item+2] == 3:
           return True;
    return False;

print array123([1, 1, 2, 3, 1]);
print array123([1, 1, 2, 4, 1]);
print array123([1, 1, 2, 1, 2, 3]);

