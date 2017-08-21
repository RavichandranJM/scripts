def front_times(string, times):
    front_length = 3;
    if front_length > len(string):
        front_length = len(string)
    front=string[:front_length];
    return front * times;

print front_times('Chocolate', 2);
print front_times('Chocolate', 3);
print front_times('Abc', 3);

