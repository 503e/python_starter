from utils import add_numbers, greet, calculate_mean


def main():
    print("Example Project Running!")

    result = add_numbers(5, 7)
    print(f"5 + 7 = {result}")

    message = greet("Point Loma, this is Luke")
    print(message)

    numbers = [10, 20, 30, 40]
    mean_value = calculate_mean(numbers)
    print(f"The mean of {numbers} is {mean_value}")


if __name__ == "__main__":
    main()
