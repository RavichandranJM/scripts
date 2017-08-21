def count_evens(nums):
    count = 0;
    for num in nums:
        if num % 2 == 0:
            count += 1;
    return count;

def big_diff(nums):
    return max(nums) - min(nums);

def centered_average(nums):
    nums.remove(min(nums));
    nums.remove(max(nums));
    return sum(nums)/len(nums);

def sum13(nums):
    count = len(nums);
    index = 0;
    sum = 0;
    while(index < count):
        if nums[index] == 13 or nums[index-1] == 13:
            continue;
        sum += nums[index];
        index += 1;
    return sum;

print sum13([1, 2, 2, 1]);

def sum67(nums):
    skipFlag = False;
    count = len(nums);
    index = 0;
    sum = 0;
    while (index < count):
        if nums[index] == 6:
            skipFlag = True;
        if(not skipFlag):
            sum += nums[index];
        if nums[index] == 7:
            skipFlag = False;
        index += 1;
    return sum;

def has22(nums):
    index = 0;
    count = len(nums);
    while(index < count-1):
        if nums[index] == 2 and nums[index+1] == 2:
             return True;
        index += 1;
    return False;

  


