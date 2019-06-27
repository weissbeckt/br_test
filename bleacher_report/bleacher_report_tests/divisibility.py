def main():
    first = int(input("Enter a number between 1 and 100: "))
    second = int(input("Enter another number between 1 and 100: "))
    third = int(input("Enter yet another number between 1 and 100: "))
    print "Here are the numbers evenly divisible by at least 1 in that range for those 3 numbers (duplicates removed)"
    print divisibility_check(first, second, third)


def divisibility_check(a, b, c):
    number_list = [a, b, c]
    lower = 1
    upper = 100
    results = []

    for i in number_list:
        for j in range(lower, upper):
            if i * j <= upper:
                result = i * j
                if result not in results:
                    results.append(result)
    results.sort()
    return results


if __name__ == '__main__':
    main()
