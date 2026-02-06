def longest_positive_streak(nums: list[int]) -> int:
    """
    Return the length of the longest run of consecutive values strictly greater than 0.
    Rules:
    - Empty list returns 0.
    - Non-positive numbers (0 or negatives) break/reset the streak.
    - Must be deterministic and pure: no randomness, prints, I/O, or global state.
    """
    # A no-op change to trigger CI.
    max_run = 0
    current = 0
    for x in nums:
        if x > 0:
            current += 1
            if current > max_run:
                max_run = current
        else:
            current = 0
    return max_run