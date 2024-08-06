from random import randint
from soroban import init_rods, print_soroban, set_rods


if __name__ == "__main__":
    print(
        "How many digits do you want to add?",
        "Enter 1 (eg. 7 + 8), or",
        "Enter 2 (eg. 47 + 12), or",
        "Enter 3 (eg. 347 + 112), or",
        "Enter 4 (eg. 2347 + 6194), or",
        "Enter 5 (eg. 59187 + 19112)",
        sep="\n",
    )
    digits = int(input())
    print("Press 'q' to quit")
    while True:
        rods = init_rods()
        max = 10 ** (digits) - 1
        x = randint(1, max)
        y = randint(1, max)
        print(f"{x} + {y} = ?")
        re = input()
        if re == "q":
            break
        sum = x + y
        print(sum)
        set_rods(sum, rods)
        print_soroban(rods)
