from random import randint


def init_rods():
    ones = [0 for i in range(5)]
    tens = [0 for i in range(5)]
    hundreds = [0 for i in range(5)]
    thousands = [0 for i in range(5)]
    return thousands, hundreds, tens, ones


def set_rods(sum):
    thousands_rod, hundreds_rod, tens_rod, ones_rod = rods
    thousands_digit = (sum // 1000) % 10
    hundreds_digit = (sum // 100) % 10
    tens_digit = (sum // 10) % 10
    ones_digit = sum % 10
    if ones_digit >= 5:
        ones_rod[0] = 1
        ones_digit -= 5
    if tens_digit >= 5:
        tens_rod[0] = 1
        tens_digit -= 5
    if hundreds_digit >= 5:
        hundreds_rod[0] = 1
        hundreds_digit -= 5
    if thousands_digit >= 5:
        thousands_rod[0] = 1
        thousands_digit -= 5
    for i in range(1, ones_digit + 1):
        ones_rod[i] = 1
    for i in range(1, tens_digit + 1):
        tens_rod[i] = 1
    for i in range(1, hundreds_digit + 1):
        hundreds_rod[i] = 1
    for i in range(1, thousands_digit + 1):
        thousands_rod[i] = 1
    return


def print_soroban():
    thousands_rod, hundreds_rod, tens_rod, ones_rod = rods
    print("●", end="") if (thousands_rod[0]) else print(" ", end="")
    print("●", end="") if (hundreds_rod[0]) else print(" ", end="")
    print("●", end="") if (tens_rod[0]) else print(" ", end="")
    print("●", end="") if (ones_rod[0]) else print(" ", end="")
    print("\n––––")
    for i in range(1, 5):
        print("●", end="") if (thousands_rod[i]) else print(" ", end="")
        print("●", end="") if (hundreds_rod[i]) else print(" ", end="")
        print("●", end="") if (tens_rod[i]) else print(" ", end="")
        print("●", end="") if (ones_rod[i]) else print(" ", end="")
        print()
    print()


if __name__ == "__main__":
    print(
        "How many digits do you want to add? Enter 1 (eg. 7 + 8), 2 (eg. 47 + 12), or 3 (eg. 347 + 112)"
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
        set_rods(sum)
        print_soroban()
