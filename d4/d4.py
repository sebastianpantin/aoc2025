import numpy as np
from scipy.signal import convolve

kernel = np.ones((3, 3), dtype=np.int8)
kernel[1, 1] = 0


def p1(input: str):
    lines = input.strip().split("\n")
    arr = np.array([[int(char == "@") for char in line] for line in lines])

    neighbor_count = convolve(arr, kernel, mode="same")

    return np.sum((arr == 1) & (neighbor_count < 4))


def p2(input: str):
    lines = input.strip().split("\n")
    arr = np.array([[int(char == "@") for char in line] for line in lines])

    total_removed = 0

    changed = True
    while changed:
        neighbor_count = convolve(arr, kernel, mode="same")

        to_remove = (arr == 1) & (neighbor_count < 4)
        changed = np.any(to_remove)
        removed_count = np.sum(to_remove)
        total_removed += removed_count
        arr[to_remove] = 0

    return total_removed


def main():
    with open("d4/input.txt") as f:
        input = f.read()

    test = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

    print(f"Part 1 test: {p1(test)}")
    print(f"Part 2 test: {p2(test)}")

    print(f"Part 1: {p1(input)}")
    print(f"Part 2: {p2(input)}")


if __name__ == "__main__":
    main()
