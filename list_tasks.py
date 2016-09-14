def remove_adjacent(lst):
    new_lst = []
    if len(lst) != 0 :
     new_lst.append(lst[0])
     n = 0
     for i in range(1,len(lst)):
        if lst[i] != new_lst[n]:
            new_lst.append(lst[i])
            n += 1
    return new_lst

def linear_merge(lst1, lst2):
    new_lst = []
    k1 = 0
    k2 = 0
    while k1 < len(lst1) and k2 <len(lst2):
        if lst1[k1] <= lst2[k2]:
            new_lst.append(lst1[k1])
            k1 += 1
        else:
            new_lst.append(lst2[k2])
            k2 += 1
    if k1 == len(lst1):
        for i in range(k2,len(lst2)):
            new_lst.append(lst2[i])
    else:
        for i in range(k1,len(lst1)):
            new_lst.append(lst1[i])
    return new_lst
