import pytest
from streak import longest_positive_streak

def test_empty_input():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_wins():
    nums = [1, 2, 0, 3, 4, 5, -2, 1, 1]
    # streaks: [1,2] -> 2; [3,4,5] -> 3; [-2] breaks; [1,1] -> 2
    assert longest_positive_streak(nums) == 3

def test_contains_zeros_and_negatives():
    nums = [0, -1, 2, 0, -3, 4, 5, 0]
    assert longest_positive_streak(nums) == 2

def test_all_positive():
    nums = [1, 1, 1, 1]
    assert longest_positive_streak(nums) == 4

def test_all_non_positive():
    nums = [0, 0, -1, -5, 0]
    assert longest_positive_streak(nums) == 0

def test_single_values():
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-3]) == 0

def test_alternate_pos_and_zero():
    nums = [1, 0, 1, 0, 1]
    assert longest_positive_streak(nums) == 1