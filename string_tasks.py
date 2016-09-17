def verbing(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"
    return s


def not_bad(s):
    s1 = s.find("not")
    s2 = s.find("bad")
    if s2 > s1 > -1:
            s = s[:s1] + "good" + s[s2+3:]
    return s


def front_back(a, b):
    n1 = (len(a) + 1) // 2
    n2 = (len(a) + 1) // 2
    a_front = a[:n1]
    a_back = a[n1:]
    b_front = b[:n2]
    b_back = b[n2:]
    return a_front + b_front + a_back + b_back
