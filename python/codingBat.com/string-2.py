def double_char(str):
    doublestr = "";
    for char in str:
        doublestr += char + char;
    return doublestr;

def count_hi(str):
    count = 0;
    for index in range(len(str-1)):
        if str[index:index+2] == "hi" :
            count += 1;
    return count;


def cat_dog(str):
    catCount = 0;
    dogCount = 0;
    for index in range(len(str)-2):
        if str[index:index+3] == "cat":
            catCount += 1;
        elif str[index:index+3] == "dog":
            dogCount += 1;
    if catCount == dogCount:
        return True;
    return False;

def count_code(str):
    count = 0;
    for index in range(len(str)-3):
        if str[index:index+2] == "co" and str[index+3] == "e":
            count += 1;
    return count;

def end_other(a, b):
    al = a.lower();
    bl = b.lower();
    if bl.endswith(al) or al.endswith(bl):
        return True;
    return False;

def xyz_there(str):
    for index in range(len(str)-2):
        if str[index:index+3] == "xyz":
            if str[index-1] != None and str[index-1] == ".":
                continue;
            return True;
    return False;
