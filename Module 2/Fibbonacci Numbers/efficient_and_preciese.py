def fibonacci_sequence(n):
    sequence = []
    # first two fibonacci numbers
    a, b = 1, 1
    # generate the fibonacci numbers till n, using first two fibonacci numbers
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    # return the nth number
    return sequence[n - 1]


if __name__ == '__main__':
    _ = int(input())
    print(fibonacci_sequence(_))

