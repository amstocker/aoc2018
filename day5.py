from string import ascii_lowercase

def reduce_once(s):
    parts = []
    last = 0
    i = 0
    while i < len(s)-1:
        if (s[i].lower() == s[i+1].lower()) and \
                ((s[i].islower() and s[i+1].isupper()) \
                 or \
                 (s[i].isupper() and s[i+1].islower())):
            parts.append(s[last:i])
            last = i + 2
            i += 2
        else:
            i += 1
    parts.append(s[last:])
    return ''.join(parts)

def reduce_all(s):
    last = s + "padding"
    while len(last) - len(s) > 0:
        last = s
        s = reduce_once(s)
    return last

def cfilter(s, c):
    return ''.join(k for k in s if k.lower() != c.lower())

with open("day5_input.txt") as f:
    s = f.read().rstrip()
    
    # part 1
    print(len(reduce_all(s)))

    # part 2
    print(min(map(lambda c: len(reduce_all(cfilter(s, c))), ascii_lowercase)))
