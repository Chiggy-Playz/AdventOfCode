from utils.input_manager import get_input
from utils.stats import benchmark
from utils.timing import timeit
from utils.types import InputType


def part1(lines: InputType):
    values = []
    for line in lines:
        test_raw, nums = line.split(": ")
        test = int(test_raw)
        (*nums,) = map(int, nums.split())

        def find(nums: list[int], val: int):
            if len(nums) == 1:
                return nums[-1] == val

            if val % nums[-1] == 0 and find(nums[:-1], val // nums[-1]):
                return True

            if val - nums[-1] > 0 and find(nums[:-1], val - nums[-1]):
                return True

            return False

        if find(nums, test):
            values.append(test)

    return sum(values)


def part2(lines: InputType):
    values = []
    for line in lines:
        test_raw, nums = line.split(": ")
        test = int(test_raw)
        (*nums,) = map(int, nums.split())

        def find(nums: list[int], val: int):
            if len(nums) == 1:
                return nums[-1] == val

            if val % nums[-1] == 0 and find(nums[:-1], val // nums[-1]):
                return True

            if val - nums[-1] > 0 and find(nums[:-1], val - nums[-1]):
                return True

            if (
                str(val).endswith(str(nums[-1]))
                and (new_val := str(val)[: -len(str(nums[-1]))])
                and find(nums[:-1], int(new_val))
            ):
                return True

            return False

        if find(nums, test):
            values.append(test)

    return sum(values)


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    benchmark(main, lines)

    """
    850435817339
    Part 1 took 3.18 ms
    104824810233437
    Part 2 took 6.08 ms

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 8.98 ms
    """
