import pytest
from geometry.shapes import Square, Circle
from geometry.utils import area_stats
def test_square_area_zero_and_positive():
    #Arrange
    sq_zero=Square(0)
    sq_int=Square(3)
    sq_float=Square(2.5)

    #Act
    area_zero = sq_zero.area()
    area_int = sq_int.area()
    area_float = sq_float.area()

    #Assert
    assert area_zero == pytest.approx(0.0)
    assert area_int == pytest.approx(9.0)
    assert area_float == pytest.approx(6.25)

def test_circle_area_zero_and_positive():
    #Arrange
    c_zero=Circle(0)
    c_int=Circle(1)
    c_float=Circle(2.5)

    #Act
    area_zero = c_zero.area()
    area_int = c_int.area()
    area_float = c_float.area()

    #Assert
    assert area_zero == pytest.approx(0.0)
    assert area_int == pytest.approx(3.1415926)
    assert area_float == pytest.approx(19.63495408)

def test_stats_keys_and_values():
    #Arrange
    shapes = [Square(2),Circle(1), Square(1.5)]
    areas = [s.area() for s in shapes]
    expected_n=len(areas)
    expected_total = sum(areas)
    expected_mean = expected_total/expected_n
    expected_max=max(areas)
    expected_min=min(areas)
    stats = area_stats(*shapes)

    assert stats['n']==expected_n
    assert stats['total']==expected_total
    assert stats['mean']==expected_mean

    assert stats['max']==expected_max
    assert stats['min']==expected_min

def test_stats_raises_without_shapes():
    with pytest.raises(ValueError, match="At least one Shape is required"):
        area_stats()
