def last2(string):
    count = 0;
    # if string has two char
    if(len(string) < 2):
        return count;
    # if string more than two char
    substr = string[-2:];
    #check substring length start from index
    for index in range(len(string)-2):
        substr = string[index:index+2];
    print substr;
last2('hidkfjdhidbfjdhikkkkkkihi');
