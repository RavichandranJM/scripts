def make_bricks(small, big, goal):
    coeff = goal / 5;
    if coeff >= big:
        remain = goal - big * 5;
    else:
        remain = goal - coeff * 5;
    if remain <= small:
        return True;
    return False;

def lone_sum(a, b, c):
    sum = 0;
    if a != b and a != c:
        sum += a;
    if b != a and b != c:
        sum += b;
    if c != a and c != b:
        sum += c;
    return sum;

def lucky_sum(a, b, c):
    sum = 0;
    for num in a, b, c:
        if num != 13 :
            sum += num;
        else:
            break;     
    return sum;
    
def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c);
    
def fix_teen(n):
    teenList = [13,14, 17, 18, 19];
    if n in teenList:
        return 0;
    return n;

def round_sum(a, b, c):
    return round10(a) + round10(b)+ round10(c);

def round10(num):
    mod = num % 10;
    num = num - mod;
    if mod >= 5:
        num += 10;
    return num;

def close_far(a, b, c):
    if abs(a - b) <= 1:
        if abs(a - c) >= 2 and abs(b - c) >= 2:
            return True;
    elif abs(a - c) <= 1:
        if abs(a - b) >= 2 and abs(b - c) >= 2:
            return True;
    return False;


def make_chocolate(small, big, goal):
    coeff = goal / 5;
    if coeff <= big:
       remain = goal - coeff * 5
    else:
       remain = goal - big * 5;
    if remain <= small:
        return remain;
    else:
        return -1;
