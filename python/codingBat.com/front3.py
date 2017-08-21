def front3(ostr):
    front_end = 3;
    if (len(ostr) < 3):
        front_end = len(ostr);
    front = ostr[:front_end];
    return front * 3;

print front3('Java');
print front3('Chocolate');
print front3('ab');
