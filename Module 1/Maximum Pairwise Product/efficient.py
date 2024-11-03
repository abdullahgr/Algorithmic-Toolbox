def maximum_pairwise_product_fast(n, numbers):
    index_1 = -1
    index_2 = -1
    for i in range(n):
        if index_1 == -1 or numbers[i] > numbers[index_1]:
            index_1 = i
    for j in range(n):
        if j != index_1 and (index_2 == -1 or numbers[j] > numbers[index_2]):
            index_2 = j
    return numbers[index_1] * numbers[index_2]

if __name__ == '__main__':
    size = int(input())
    numbers_array = list(map(int, input().split()))
    print(maximum_pairwise_product_fast(size, numbers_array))


# the first input parameter is the size of the number array
# second input parameter is the numbers array itself, separated by commas

# the input numbers element's range is 0 < number <= 2 * 10**5