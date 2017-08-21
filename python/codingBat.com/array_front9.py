def array_front9(nums):
    num = 9;
    if num in nums[:4]:
        return True;
    return False;

print array_front9([1, 2, 9, 3, 4]);
print array_front9([1, 2]);
print array_front9([1, 2, 3, 4, 9]);
