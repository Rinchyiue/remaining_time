def compute_remaining_time(end_time, current_time):
    return end_time - current_time


def test_remaining_time():
    assert compute_remaining_time(10, 7) == 3
