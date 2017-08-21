def string_match(a, b):
    shorter = min(len(a), len(b));
    count = 0;
    for item in range(shorter-1):
        aSub = a[item:item+2];
        bSub = b[item:item+2];
        if aSub == bSub:
            count += 1;
    return count;

print string_match('xxcaazz', 'xxbaaz');
print string_match('abc', 'abc');
print string_match('abc', 'axc');
