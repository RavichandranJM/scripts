def extra_end(string):
    end = string[len(string)-2:];
    return end * 3;
print "extra_end";
print extra_end('Hello');
print extra_end('ab');
print extra_end('Hi');

def first_two(string):
    twoChar = string[:2];
    return twoChar;
print "first_two";
print first_two('Hello');
print first_two('abcdefg');
print first_two('x');


def first_half(string):
    split = len(string)/2;
    return string[:split];
print "first_half";
print first_half('Woohoo');
print first_half('HelloThere');
print first_half('abcdef');


def without_end(string):
    return string[1:-1];
print "without_end";
print without_end('Hello');
print without_end('java');
print without_end('coding');

def combo_string(a, b):
    if(len(a) < len(b)):
        sStr = a;
        lStr = b;
    else:
        lStr = a;
        sStr = b;
    return sStr + lStr + sStr;
print combo_string('Hello', 'Hi');
print combo_string('hi', 'Hello');
print combo_string('aaa', 'b');

def non_start(a, b):
    return a[1:] + b[1:];

print non_start('Hello', 'There');
print non_start('java', 'code');
print non_start('shotl', 'java');

def left2(string):
    return string[2:] + string[:2];


print left2('hello');
print left2('java');
print left2('he');
