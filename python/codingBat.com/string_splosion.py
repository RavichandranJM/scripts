def string_splosion(string):
    result = "";
    for endIndex in range(len(string)):
        result = result + string[0:endIndex+1];
    return result;
print string_splosion('Code');
print string_splosion('abc');
print string_splosion('ab');

