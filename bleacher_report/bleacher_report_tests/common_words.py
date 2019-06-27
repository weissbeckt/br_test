# A few examples here of different functions to accomplish the word compare
def main():
    list_a = ["trying", "to", "think", "of", "a", "song", "lyric"]
    list_b = ["unfortunately", "no", "lyric", "for", "any", "song", "comes", "to", "mind"]
    print "A few different ways to do it: "
    print compare(list_a, list_b)
    print compare_efficiently(list_a, list_b)
    print compare_efficiently_reversed(list_a, list_b)


def compare(first, second):
    return list(set(first) & set(second))


def compare_efficiently(list_a, list_b):
    tmp = set(list_a)
    list_c = [value for value in list_b if value in tmp]
    return list_c


def compare_efficiently_reversed(list_a, list_b):
    tmp = set(list_b)
    list_c = [value for value in list_a if value in tmp]
    return list_c


if __name__ == '__main__':
    main()
