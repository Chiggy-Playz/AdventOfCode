from utils.input_manager import get_input

input = get_input(__file__)

safe = 0


def get_diffs(report: list[int]):
    diffs = []
    for a, b in zip(report, report[1:]):
        diffs.append(a - b)
    return diffs


def verify(report: list[int]):
    diffs = get_diffs(report)
    diff_check = all([1 <= abs(diff) <= 3 for diff in diffs])
    if not diff_check:
        return False

    sign_check = sum([abs(diff) // diff for diff in diffs]) in (len(diffs), -len(diffs))

    return sign_check


for report in input:
    report = [int(x) for x in report.split()]
    if verify(report):
        safe += 1
        continue

    i = 0
    # Bruteforce
    while i < (len(report)):
        modified_report = report[:i] + report[i + 1 :]
        verification = verify(modified_report)
        if verification:
            safe += 1
            break
        i += 1

print(safe)
