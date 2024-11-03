def maximum_pairwise_product_slow(n, numbers):
    product = 0
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] * numbers[j] > product:
                product = numbers[i] * numbers[j]
    return product

if __name__ == '__main__':
    size = int(input())
    numbers_array = list(map(int, input().split()))
    print(maximum_pairwise_product_slow(size, numbers_array))


# the first input parameter is the size of the number array
# second input parameter is the numbers array itself, separated by commas

# the input numbers element's range is 0 < number <= 2 * 10**5