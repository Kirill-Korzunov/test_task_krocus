from test_task.solution import get_max_positive_sequence

def test_get_max_positive_sequence_empty():
    assert get_max_positive_sequence([]) == 0


def test_get_max_positive_sequence_only_negative():
    assert get_max_positive_sequence(iter([ ['-1'], ['-2'], ['-3'], ['-6'] ])) == 0


def test_get_max_positive_sequence():
    assert get_max_positive_sequence(iter([ ['1'], ['-2'], ['3'], ['6'] ])) == 2