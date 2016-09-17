import sys


def read_words(filename):
    words = []
    with open(filename, "r") as f:
        for line in f:
            words.extend(line.split())
    return words


def create_list_of_words(filename):
    d={}
    for i in read_words(filename):
        s = i.lower()
        d[s] = d.get(s, 0) + 1
    return list(d.items())


def print_words(filename):
    a = create_list_of_words(filename)
    a.sort()
    for key, value in a:
        print(key, value)


def print_top(filename):
    a = create_list_of_words(filename)
    a.sort(key=lambda x: -x[1])
    for key, value in a[:20]:
        print(value, key)


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
