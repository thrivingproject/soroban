def init_rods():
    ones = [0 for i in range(5)]
    tens = [0 for i in range(5)]
    hundreds = [0 for i in range(5)]
    thousands = [0 for i in range(5)]
    ten_thousands = [0 for i in range(5)]
    hundred_thousands = [0 for i in range(5)]
    millions = [0 for i in range(5)]
    return millions, hundred_thousands, ten_thousands, thousands, hundreds, tens, ones


def set_rods(value, rods):
    (
        millions_rod,
        hundred_thousands_rod,
        ten_thousands_rod,
        thousands_rod,
        hundreds_rod,
        tens_rod,
        ones_rod,
    ) = rods
    millions_digit = (value // 1000000) % 10
    hundred_thousands_digit = (value // 100000) % 10
    ten_thousands_digit = (value // 10000) % 10
    thousands_digit = (value // 1000) % 10
    hundreds_digit = (value // 100) % 10
    tens_digit = (value // 10) % 10
    ones_digit = value % 10
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
    if ten_thousands_digit >= 5:
        ten_thousands_rod[0] = 1
        ten_thousands_digit -= 5
    if hundred_thousands_digit >= 5:
        hundred_thousands_rod[0] = 1
        hundred_thousands_digit -= 5
    if millions_digit >= 5:
        millions_rod[0] = 1
        millions_digit -= 5
    for i in range(1, ones_digit + 1):
        ones_rod[i] = 1
    for i in range(1, tens_digit + 1):
        tens_rod[i] = 1
    for i in range(1, hundreds_digit + 1):
        hundreds_rod[i] = 1
    for i in range(1, thousands_digit + 1):
        thousands_rod[i] = 1
    for i in range(1, ten_thousands_digit + 1):
        ten_thousands_rod[i] = 1
    for i in range(1, hundred_thousands_digit + 1):
        hundred_thousands_rod[i] = 1
    for i in range(1, millions_digit + 1):
        millions_rod[i] = 1
    return


def print_soroban(rods):
    (
        millions_rod,
        hundred_thousands_rod,
        ten_thousands_rod,
        thousands_rod,
        hundreds_rod,
        tens_rod,
        ones_rod,
    ) = rods
    print("●", end="") if (millions_rod[0]) else print(" ", end="")
    print("●", end="") if (hundred_thousands_rod[0]) else print(" ", end="")
    print("●", end="") if (ten_thousands_rod[0]) else print(" ", end="")
    print("●", end="") if (thousands_rod[0]) else print(" ", end="")
    print("●", end="") if (hundreds_rod[0]) else print(" ", end="")
    print("●", end="") if (tens_rod[0]) else print(" ", end="")
    print("●", end="") if (ones_rod[0]) else print(" ", end="")
    print("\n–––––––")
    for i in range(1, 5):
        print("●", end="") if (millions_rod[i]) else print(" ", end="")
        print("●", end="") if (hundred_thousands_rod[i]) else print(" ", end="")
        print("●", end="") if (ten_thousands_rod[i]) else print(" ", end="")
        print("●", end="") if (thousands_rod[i]) else print(" ", end="")
        print("●", end="") if (hundreds_rod[i]) else print(" ", end="")
        print("●", end="") if (tens_rod[i]) else print(" ", end="")
        print("●", end="") if (ones_rod[i]) else print(" ", end="")
        print()
    print()


def show_soroban():
    answer = input("Do you want to see the soroban? (y/n) ")
    if answer == "y":
        return True
    return False
