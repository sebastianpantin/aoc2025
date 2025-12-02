def is_repetition_part_1(num):
    s = str(num)
    half = len(s) // 2
    return num if len(s) % 2 == 0 and s[:half] == s[half:] else 0

def is_repetition_part_2(num):
    s = str(num)
    n = len(s)
    for d in range(1, n // 2 + 1):
        if n % d == 0 and s == s[:d] * (n // d):
            return num
    return 0


def p1(input: str):
    total_invalids = 0
    intervals = [interval.strip() for interval in input.split(",")]
    for interval in intervals:
        low, high = interval.split("-")
        for num in range(int(low), int(high) + 1):
            total_invalids += is_repetition_part_1(num)

    return total_invalids


def p2(input: str):
    total_invalids = 0
    intervals = [interval.strip() for interval in input.split(",")]
    for interval in intervals:
        low, high = interval.split("-")
        for num in range(int(low), int(high) + 1):
            total_invalids += is_repetition_part_2(num)

    return total_invalids


def main():
    with open("d2/input.txt") as f:
        input = f.read()

    test = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
