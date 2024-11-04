def get_greatest_common_divisor(first, second):
    # Find minimum of a and b
    result = min(a, b)

    while result:
        if a % result == 0 and b % result == 0:
            break
        result -= 1

    # Return the gcd of a and b
    return result

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(get_greatest_common_divisor(a, b))
