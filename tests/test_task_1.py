import pytest
from typing import List, Tuple
from src.task_1 import find_min_max


@pytest.mark.parametrize(
    "arr,expected",
    [
        # 1. Normal list
        ([8, 2, 1, 4, -5, 12, 22, 36], (-5, 36)),
        # 2. Single element
        ([1], (1, 1)),
        # 3. All identical elements
        ([2, 2, 2, 2], (2, 2)),
        # 4. All negative numbers
        ([-1, -5, -3, -4], (-5, -1)),
        # 5. Two elements
        ([100, -100], (-100, 100)),
        # 6. Large ascending list
        (list(range(1000)), (0, 999)),
        # 7. Large descending list
        (list(range(1000, 0, -1)), (1, 1000)),
        # 8. Small odd-length list
        ([7, 3, 9], (3, 9)),
        # 9. Small even-length list
        ([5, 8, 2, 9], (2, 9)),
        # 10. Mixed positives and negatives
        ([-10, 5, 0, 12, -3], (-10, 12)),
    ],
)
def test_find_min_max(arr: List[int], expected: Tuple[int, int]):
    if len(arr) == 1:
        result = (arr[0], arr[0])
    else:
        result = find_min_max(arr, 0, len(arr) - 1)
    assert result == expected
