from geometry.shapes import Square, Circle
from geometry.utils import area_stats

#Shape Construction
sq_float=Square(2.5)
c_float=Circle(2.5)
#Shape Area Printing
sq_area_float = sq_float.area()
print(sq_area_float)

sq_area_float = c_float.area()
print(sq_area_float)
#Summary Dict Printing
shapes = [sq_float,c_float]
print(area_stats(*shapes))