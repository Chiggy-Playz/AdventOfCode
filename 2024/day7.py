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
        found = False

        def find(stack: list[int], nums: list[int]):
            nonlocal found
            if found:
                return

            if not nums:
                if stack.pop() == test:
                    values.append(test)
                    found = True
                return

            if not stack:
                stack.append(nums.pop(0))

            if len(stack) < 2:
                stack.append(nums.pop(0))

            # Stack has 2 things. Add and multiply
            add = stack[0] + stack[1]
            prod = stack[0] * stack[1]
            if add <= test:
                find([add, *stack[2:]], nums.copy())
            if prod <= test:
                find([prod, *stack[2:]], nums.copy())

        find([], nums)

    return sum(values)


def part2(lines: InputType):
    values = []
    for line in lines:
        test_raw, nums = line.split(": ")
        test = int(test_raw)
        (*nums,) = map(int, nums.split())
        found = False

        def find(stack: list[int], nums: list[int]):
            nonlocal found
            if found:
                return

            if not nums:
                if stack.pop() == test:
                    values.append(test)
                    found = True
                return

            if not stack:
                stack.append(nums.pop(0))

            if len(stack) < 2:
                stack.append(nums.pop(0))

            # Stack has 2 things. Add and multiply and concat
            add = stack[0] + stack[1]
            prod = stack[0] * stack[1]
            concat = int(f"{stack[0]}{stack[1]}")
            if add <= test:
                find([add, *stack[2:]], nums.copy())
            if prod <= test:
                find([prod, *stack[2:]], nums.copy())
            if concat <= test:
                find([concat, *stack[2:]], nums.copy())

        find([], nums)

    return sum(values)


def main(lines: InputType):
    with timeit("Part 1"):
        print(part1(lines))

    with timeit("Part 2"):
        print(part2(lines))


if __name__ == "__main__":
    lines = get_input(testing=False)
    main(lines)
    # benchmark(main, lines)

    """
    850435817339
    Part 1 took 60.99 ms
    104824810233437
    Part 2 took 1.79 s

    --- Benchmarks ---
    Number of runs: 100
    Average per run: 1.84 s
    """