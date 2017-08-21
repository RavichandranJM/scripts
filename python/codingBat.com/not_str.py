#! /usr/bin/python

def not_str(str):
    if len(str) >= 3 and str[:3] == "not":
        return str;
    return ("not " + str);

print not_str('candy');
print not_str('x');
print not_str('bad not');
