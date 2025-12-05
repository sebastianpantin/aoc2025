def p1(input: str):
    ranges, ids = input.strip().split("\n\n")
    fresh = 0
    for id in ids.split("\n"):
        if id:
            for line in ranges.strip().splitlines():
                low, high = map(int, line.split("-"))
                if int(id) >= int(low) and int(id) <= int(high):
                    fresh += 1
                    break
    return fresh


def p2(input: str):
    ranges = input.strip().split("\n\n")[0].strip().splitlines()
    all_intervals: list[tuple[int, int]] = []
    for line in ranges:
        low, high = map(int, line.split("-"))
        all_intervals.append((low, high))

    all_intervals.sort()
    merged: list[list[int]] = []
    for low, high in all_intervals:
        if not merged or merged[-1][1] < low - 1:
            merged.append([low, high])
        else:
            merged[-1][1] = max(merged[-1][1], high)

    return sum(high - low + 1 for low, high in merged)


def main():
    with open("d5/input.txt") as f:
        input = f.read()

    test = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")
    #
    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
