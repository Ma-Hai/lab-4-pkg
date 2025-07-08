import pytest, math
from geometry import Square, Circle, area_stats
def test_square_area_zero_and_positive():
    c = Square(side=2)
    assert (c.area()==4)
    d= Circle(side=4)
    assert (d.area()==16*math.pi)
 # Arrange: choose side lengths
 # Act: compute areas
 # Assert: use pytest.approx to compare with expected
# def test_stats_keys_and_values():
#     area_stats(Circle,Square)
#  # Arrange: create several shapes
#  # Act: call area_stats
#  # Assert: stats is dict, has correct keys, and values are numbers
# def test_stats_raises_without_shapes():
#     assert(area_stats()== ValueError("At least one Shape is required")) 
#  # Assert that calling area_stats() raises ValueError