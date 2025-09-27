# goit-algo2-hw-02
Design and Analysis of Algorithms

## Task 1: Finding Maximum and Minimum Elements

### Objective

Implement a function to find the maximum and minimum elements in an array using the Divide and Conquer method.

### Acceptance Criteria

* The function accepts an array of numbers of any length (10 points).
* A recursive approach is used (10 points).
* Returns a tuple of values `(minimum, maximum)` (10 points).
* Algorithm complexity is O(n) (10 points).

### Example Usage

```python
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
min_val, max_val = find_min_max(arr)
print(min_val, max_val)  # Output: 1 9
```

---

## Task 2: 3D Printer Queue Optimization

### Objective

Develop a program to optimize a 3D printer task queue in a university lab, considering priorities and technical constraints using a greedy algorithm.

### Task Description

1. Input data is a list of print jobs, each containing: ID, model volume, priority, and print time.
2. Implement the main function `optimize_printing` which should:

   * Consider task priorities.
   * Group models for simultaneous printing.
   * Check volume and item constraints.
   * Calculate total print time.
   * Return the optimal print order.
3. Output the optimal print order and the total time required to complete all tasks.

### Input Format

```python
print_jobs = [
    {
        "id": str,       # unique identifier
        "volume": float, # volume in cm³ (> 0)
        "priority": int, # priority (1, 2, or 3)
        "print_time": int # print time in minutes (> 0)
    }
]

printer_constraints = {
    "max_volume": float, # maximum printable volume
    "max_items": int     # maximum number of models
}
```

### Priority Levels

1. Highest — Course/Thesis projects
2. Medium — Lab works
3. Lowest — Personal projects

### Output Format

```python
{
    "print_order": ["M1", "M2", "M3"],  # order of printing jobs
    "total_time": 360  # total time in minutes
}
```

### Example Usage

```python
result = optimize_printing(print_jobs, printer_constraints)
print(result["print_order"])
print(result["total_time"])
```
