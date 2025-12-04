def get_max_joltage(bank, digits):
        if digits == 1:
            return max(bank)
        digit = max(bank[:1-digits])
        i = bank.index(digit) + 1
        return digit + get_max_joltage(bank[i:], digits - 1)

def p1(input: str):
    lines = [line.strip() for line in input.split("\n")]
    total = 0
    for line in lines:
        if not line:
            continue
        total += int(get_max_joltage(line, 2))

    return total


def p2(input: str):
    lines = [line.strip() for line in input.split("\n")]
    total = 0
    for line in lines:
        if not line:
            continue
        total += int(get_max_joltage(line, 12))

    return total


def main():
    with open("d3/input.txt") as f:
        input = f.read()

    test = """
    987654321111111
811111111111119
234234234234278
818181911112111
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
