import pytest
from src.task_2 import optimize_printing  # replace with actual module


@pytest.mark.parametrize(
    "jobs,constraints,expected_order,expected_time",
    [
        # 1. All same priority, can group some
        (
            [
                {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
                {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                {"id": "M3", "volume": 120, "priority": 1, "print_time": 150},
            ],
            {"max_volume": 300, "max_items": 2},
            ["M1", "M2", "M3"],
            270,  # M1+M2 (120), M3 alone (150)
        ),
        # 2. Mixed priorities
        (
            [
                {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},
                {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
                {"id": "M3", "volume": 120, "priority": 3, "print_time": 150},
            ],
            {"max_volume": 300, "max_items": 2},
            ["M2", "M1", "M3"],
            270,  # M2+M1 (max 120), M3 alone (150)
        ),
        # 3. Exceeding volume constraints
        (
            [
                {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
                {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
                {"id": "M3", "volume": 180, "priority": 2, "print_time": 120},
            ],
            {"max_volume": 300, "max_items": 2},
            ["M1", "M2", "M3"],
            450,  # each printed alone due to volume
        ),
        # 4. Single job
        (
            [{"id": "M1", "volume": 100, "priority": 1, "print_time": 60}],
            {"max_volume": 200, "max_items": 2},
            ["M1"],
            60,
        ),
        # 5. Empty list
        ([], {"max_volume": 300, "max_items": 2}, [], 0),
        # 6. Max items constraint
        (
            [
                {"id": "M1", "volume": 50, "priority": 1, "print_time": 30},
                {"id": "M2", "volume": 50, "priority": 1, "print_time": 20},
                {"id": "M3", "volume": 50, "priority": 1, "print_time": 40},
            ],
            {"max_volume": 300, "max_items": 2},
            ["M1", "M2", "M3"],
            70,  # M1+M2 (max 30), M3 alone (40)
        ),
        # 7. Job volume larger than max_volume
        (
            [{"id": "M1", "volume": 500, "priority": 1, "print_time": 100}],
            {"max_volume": 300, "max_items": 2},
            ["M1"],
            100,
        ),
        # 8. Jobs with same efficiency
        (
            [
                {"id": "M1", "volume": 100, "priority": 1, "print_time": 100},
                {"id": "M2", "volume": 200, "priority": 1, "print_time": 200},
            ],
            {"max_volume": 500, "max_items": 2},
            ["M1", "M2"],
            200,
        ),
        # 9. Multiple groups
        (
            [
                {"id": "M1", "volume": 100, "priority": 1, "print_time": 50},
                {"id": "M2", "volume": 150, "priority": 1, "print_time": 60},
                {"id": "M3", "volume": 120, "priority": 1, "print_time": 70},
            ],
            {"max_volume": 200, "max_items": 2},
            ["M1", "M2", "M3"],
            180,  # group1: M1+M2 (max 60), group2: M3 (70)
        ),
        # 10. Jobs with different priorities but same volume
        (
            [
                {"id": "M1", "volume": 100, "priority": 2, "print_time": 50},
                {"id": "M2", "volume": 100, "priority": 1, "print_time": 60},
                {"id": "M3", "volume": 100, "priority": 3, "print_time": 70},
            ],
            {"max_volume": 300, "max_items": 2},
            ["M2", "M1", "M3"],
            130,  # group1: M2+M1 (max 60), group2: M3 alone (70)
        ),
    ],
)
def test_optimize_printing(jobs, constraints, expected_order, expected_time):
    result = optimize_printing(jobs, constraints)
    assert result["print_order"] == expected_order
    assert result["total_time"] == expected_time
