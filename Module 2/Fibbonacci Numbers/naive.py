def generate_nth_fibonacci_numbers(number):
    if number == 0:
        return 0
    if number == 1:
        return 1
    return generate_nth_fibonacci_numbers(number - 2) + generate_nth_fibonacci_numbers(number - 1)

if __name__ == '__main__':
    _ = int(input())
    print(generate_nth_fibonacci_numbers(_))


# the number of statements going to be executed to generate nth fibonacci number is ~= n**2