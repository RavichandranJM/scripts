def first_last6(arr):
    if arr[0] == 6 or arr[-1] == 6:
        return True;
    return False;

print "fist_last6"
print first_last6([1, 2, 6]);
print first_last6([6, 1, 2, 3]);
print first_last6([13, 6, 1, 2, 5]);

def same_first_last(arr):
    if len(arr) >= 1 and arr[0] == arr[-1]:
        return True;
    return False;

print "same_first_last"
print same_first_last([1, 2, 3]);
print same_first_last([1, 2, 3, 1]);
print same_first_last([ ]);

def common_end(list1, list2):
    if list1[0] == list2[0] or list1[-1] == list2[-1]:
        return True;
    return False;

print "common_end";
print common_end([1, 2, 3], [7, 3]);
print common_end([1, 2, 3], [7, 3, 2]);
print common_end([1, 2, 3], [1, 3]);

def sum3(arr):
    return sum(arr);

print "sum3";
print sum3([1, 2, 3]);

def rotate_left3(arr):
    return [arr[1], arr[2], arr[0]];

print "rotate_left3"
print rotate_left3([1, 2, 3]);

def reverse3(nums):
    nums.reverse();
    return nums;

print "reverse3";
print reverse3([1, 2, 3]);

def max_end3(nums):
    num1 = max(nums);
    return [num1, num1,num1];

print "max_end3"
print max_end3([1, 2, 3]);


def sum2(arr):
    if len(arr) == 0:
        return 0;
    elif len(arr) == 1:
        return arr[0];
    else:
        return arr[0] + arr[1];

print "sum2";
print sum2([1, 2, 3]);

