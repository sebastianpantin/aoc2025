START_NUMBER = 50


def p1(input: str):
    dial = START_NUMBER
    zeroes = 0
    for line in input.strip().split("\n"):
        direction, num = line[0].upper(), int(line[1:])
        dial = (dial + num * (1 if direction == "R" else -1)) % 100
        zeroes += dial == 0
    return zeroes


def p2(input: str):
    dial = START_NUMBER
    wraps = 0
    for line in input.strip().split("\n"):
        direction, num = line[0].upper(), int(line[1:])
        delta = num * (1 if direction == "R" else -1)
        new_dial = dial + delta
        wraps += abs(new_dial // 100)
        dial = new_dial % 100
    return wraps


def main():
    with open("d1/input.txt") as f:
        input = f.read()

    test = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
