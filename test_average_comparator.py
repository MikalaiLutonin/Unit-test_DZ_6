import pytest
from average_comparator import AverageComparator

@pytest.fixture
def avg_comp():
    return AverageComparator()

def test_compare_average_list1_greater(avg_comp):
    assert avg_comp.compare_averages([1, 2, 3], [1, 2, 2]) == "Первый список имеет большее среднее значение"

def test_compare_average_list2_greater(avg_comp):
    assert avg_comp.compare_averages([1, 2, 3], [1, 3, 3]) == "Второй список имеет большее среднее значение"

def test_compare_average_lists_equal(avg_comp):
    assert avg_comp.compare_averages([1, 2, 3], [1, 2, 3]) == "Средние значения равны"
