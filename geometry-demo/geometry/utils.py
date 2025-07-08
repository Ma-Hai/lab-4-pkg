def area_stats(*shapes):
    if shapes:
        raise ValueError("At least one Shape is required")
    areas = [shape.area() for shape in shapes]
    return {
    "n": len(areas),
    "total": sum(areas),
    "mean": sum(areas)/len(areas),
    "min": min(areas),
    "max": max(areas) 
    }




# def area_stats(*shapes):
#  if no shapes passed:
#  raise ValueError("At least one Shape is required")
#  areas = [ shape.area() for shape in shapes ]
#  return {
#  "n": len(areas),
#  "total": sum(areas),
#  "mean": ...,
#  "min": ...,
#  "max": 
#  }