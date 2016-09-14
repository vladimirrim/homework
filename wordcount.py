import sys


def read_words(filename):
    words = []
    with open(filename, "r") as f:
        for line in f:
            words.extend(line.split())
    return words

def print_words(filename):
    d = {}
    a = []
    for i in read_words(filename):
        s = i.lower()
        d[s] = d.get(s, 0) + 1
    for i in d.items():
        a.append((i[0], i[1]))
    a.sort()
    for a, b in a:
        print(a, b)

def print_top(filename):
    d = {}
    a = []
    for i in read_words(filename):
        s = i.lower()
        d[s] = d.get(s, 0) + 1
    for i in d.items():
        a.append((i[1], i[0]))
    a.sort(reverse = True)
    k = 0
    for a, b in a:
        if k == 20:
            break
        k += 1
        print(b, a)
        
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()