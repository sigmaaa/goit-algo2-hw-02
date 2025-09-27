from typing import List, Tuple


def find_min_max(list: List[int], left_idx: int, right_idx: int) -> Tuple[int, int]:
    if left_idx >= right_idx - 1:
        return (
            min(list[left_idx], list[right_idx]),
            max(list[left_idx], list[right_idx]),
        )

    left_value, right_value = list[left_idx], list[right_idx]
    min_value, max_value = min(left_value, right_value), max(left_value, right_value)
    recursive_result = find_min_max(list, left_idx + 1, right_idx - 1)
    return (min(min_value, recursive_result[0]), max(max_value, recursive_result[1]))


def run_tests():
    tests = [
        ([8, 2, 1, 4, -5, 12, 22, 36], (-5, 36)),
        ([1], (1, 1)),
        ([2, 2, 2, 2], (2, 2)),
        ([-1, -5, -3, -4], (-5, -1)),
        ([100, -100], (-100, 100)),
        (list(range(1000)), (0, 999)),
        (list(range(1000, 0, -1)), (1, 1000)),
        ([7, 3, 9], (3, 9)),
    ]

    for arr, expected in tests:
        if len(arr) == 1:
            result = (arr[0], arr[0])
        else:
            result = find_min_max(arr, 0, len(arr) - 1)

        print(f"arr={arr[:10]}... len={len(arr)}")
        print(f"expected={expected}, got={result}")
        print("✅ PASS" if result == expected else "❌ FAIL", end="\n\n")


if __name__ == "__main__":
    run_tests()
