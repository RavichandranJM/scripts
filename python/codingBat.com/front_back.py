def front_back(ostr):
    if len(ostr) <= 1:
        return ostr;
    mid = ostr[1:-1];
    # last + mid + first
    return ostr[-1] + mid + ostr[0];

print front_back("code");
print front_back("rvichandran");
print front_back("ab");

