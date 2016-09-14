def verbing(s):
    new_str = s
    if len(s) >= 3:
        if s[-3: ] == "ing":
            new_str += "ly"
        else:
            new_str += "ing"
    return new_str

def not_bad(s):
    s1 = s.find("not")
    s2 = s.find("bad")
    new_string = ""
    if s1 > -1 and s2 > -1:
        if s2 > s1:
            new_string = s[0:s1] + "good" + s[s2+3:]
    else:
        new_string = s
    return new_string

def front_back(a, b):
    n1 = int((len(a)+1)/2)
    n2 = int((len(b)+1)/2)
    a_front = a[: n1]
    a_back = a[n1:]
    b_front = b[:n2]
    b_back = b[n2:]
    new_lst = a_front + b_front + a_back + b_back
    return new_lst