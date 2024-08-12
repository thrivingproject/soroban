from random import randint
from soroban import init_rods, print_soroban, set_rods, show_soroban


def print_equation(numbers):
    # Convert the numbers to strings with commas as thousand separators
    num_strs = [f"{num:,}" for num in numbers]

    # Find the maximum length between the numbers
    maximum_length = max(len(num_str) for num_str in num_strs)

    # Format the strings to be right-aligned
    num_strs = [num_str.rjust(maximum_length) for num_str in num_strs]

    # Create the separator line
    separator = "—" * (
        maximum_length + 2
    )  # +2 to account for the '+ ' at the start of each line

    # Print the equation
    for i, num_str in enumerate(num_strs):
        if i == 0:
            print(f"  {num_str}")
        else:
            print(f"+ {num_str}")
    print(separator, end="")


if __name__ == "__main__":
    print(
        "How many numbers do you want to add?",
        "Enter 2 (e.g., x + y), or",
        "Enter 3 (e.g., x + y + z), or",
        "Enter 4 (e.g., x + y + z + a), or",
        "Enter 5 (e.g., x + y + z + a + b), or",
        sep="\n",
    )
    num_count = int(input())
    if not 2 <= num_count:
        print("You must add at least 2 numbers.")
        exit()
    print(
        "How many digits do you want to add?",
        "Enter 1 (eg. 7 + 8), or",
        "Enter 2 (eg. 47 + 12), or",
        "Enter 3 (eg. 347 + 112), or",
        "Enter 4 (eg. 2347 + 6194), or",
        "Enter 5 (eg. 59187 + 19112), or",
        "Enter 6 (eg. 159187 + 191112), or",
        sep="\n",
    )
    digits = int(input())
    display_soroban = show_soroban()
    print("Press 'q' to quit or press enter to continue.")

    while True:
        rods = init_rods()
        max_num = 10 ** (digits) - 1
        numbers = [randint(1, max_num) for _ in range(num_count)]
        sum_result = sum(numbers)
        print_equation(numbers)

        # Give user a chance to quit
        re = input()
        if re == "q":
            break

        # Print the sum
        sum_str = f"{sum_result:,}"
        print(f"{sum_str}")
        set_rods(sum_result, rods)
        if display_soroban:
            print_soroban(rods)
        else:
            print()
