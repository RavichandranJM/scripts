def string_bits(string):
    result = "";
    for i in range(len(string)):
        if(i % 2 == 0):
            result = result + string[i];
    return result;

print string_bits('Hello');
print string_bits('Hi');
print string_bits('Heeololeo');

