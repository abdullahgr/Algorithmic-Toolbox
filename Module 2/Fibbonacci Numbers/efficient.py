def generate_nth_fibonacci_numbers_efficient(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    # initialize the array with None
    array_of_generated_fibonacci_numbers = [None] * number

    # generate n fibonacci numbers
    for i in range(number):
        # update the initial fibonacci numbers
        if i == 0 or i == 1:
            array_of_generated_fibonacci_numbers[i] = 1
        # compute the new fibonacci numbers based on previous ones
        if array_of_generated_fibonacci_numbers[i] is None:
            array_of_generated_fibonacci_numbers[i] = array_of_generated_fibonacci_numbers[i - 1] + array_of_generated_fibonacci_numbers[i - 2]
    print(array_of_generated_fibonacci_numbers)
    return array_of_generated_fibonacci_numbers[number - 1]

if __name__ == '__main__':
    _ = int(input())
    print(generate_nth_fibonacci_numbers_efficient(_))


# the number of statements going to be executed to generate nth fibonacci number is ~= O(n)