def cigar_party(cigars, is_weekend):
    if (cigars >= 40 and cigars <= 60 and is_weekend == False):
        return True;
    elif(cigars >= 40 and is_weekend == True):
        return True;
    return False;

print "cigar party";
print cigar_party(30, False);
print cigar_party(50, False);
print cigar_party(70, True);

def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0;
    elif you > 8 or date > 8:
        return 2;
    else:
        return 1;

print "date fashion"
print date_fashion(5, 10);
print date_fashion(5, 2);
print date_fashion(5, 5);

def squirrel_play(temp, is_summer):
    if is_summer:
        if temp >= 60 and temp <= 100:
            return True;
    else:
        if temp >= 60 and temp <= 90:
            return True;
    return False;

print "squ play"
print squirrel_play(70, False);
print squirrel_play(95, False);
print squirrel_play(95, True);

def caught_speeding(speed, is_bday):
    if is_bday:
        noTickLmt = 65;
        smallTickLmt= 86;
    else:
        noTickLmt = 60;
        smallTickLmt= 81;

    if speed <= noTickLmt:
        return 0;
    elif speed <= smallTickLmt and speed > noTickLmt:
        return 1;
    else:
        return 2;

def sorta_sum(a, b):
    tot = a + b;
    if tot >= 10 and tot <= 19:
        return 20;
    return tot;

def alarm_clock(day, vacation):
    if day >= 1 and day <= 5:
        if vacation:
            return "10:00";
        else:
            return "7:00";
    else:
        if vacation:
            return "off";
        else:
            return "10:00";

def in1to10(n, outside_mode):
    if outside_mode:
        if n <= 1 or n >= 10:
            return True;
    else:
        if n >= 1 and n <= 10:
            return True;
    return False;
