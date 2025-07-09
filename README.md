*Not quite sure whether this is correct. Please give feedback on what might need
to be changed.

# Geometry
Geometry is a minimal Python package for constructing Circles and Squares 
and solving for their areas.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install geometry-demo.

```bash
pip install geometry
```

## Usage

```python
from geometry.shapes import Square, Circle
from geometry.utils import area_stats

# constructs shape and defines lengths
shape1 = Square(side_length)
shape2 = Circle(radius)
# returns area of shape
shape.area()

# Produces statistics on areas and amount of shapes
shapes = [shapes1,shapes2]
area_stats(*shapes)
```