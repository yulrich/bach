import math
import bach.geometry


# Points
point_one = bach.geometry.Point(0, 0)
point_two = bach.geometry.Point(1, 1)
result = point_one.distance(point_two)
assert(math.isclose(result, math.sqrt(2))), "Expected: sqrt(2) - Computed: {}".format(result)


# Rectangles
rectangle_one = bach.geometry.Rectangle(bach.geometry.Point(2, 2), 2, 2)
result = rectangle_one.area()
assert(result == 4), "Expected: 4 - Computed: {}".format(result)
rectangle_one.width = 0
rectangle_one.height = 0
result = rectangle_one.area()
assert(result == 0), "Expected: 0 - Computed: {}".format(result)
rectangle_one = bach.geometry.Rectangle(bach.geometry.Point(5, 5), 2.5, 3)
result = rectangle_one.area()
assert(math.isclose(result, 7.5)), "Expected: 7.5 - Computed: {}".format(result)

rectangle_one = bach.geometry.Rectangle(bach.geometry.Point(5, 5), 2.5, 3)
result = rectangle_one.contains(bach.geometry.Point(5, 5))
assert(result is True), "Expected: True - Computed: {}".format(result)
result = rectangle_one.contains(bach.geometry.Point(3.75, 4.8))
assert(result is True), "Expected: True - Computed: {}".format(result)
result = rectangle_one.contains(bach.geometry.Point(3.74, 5))
assert(result is False), "Expected: False - Computed: {}".format(result)

rectangle_one = bach.geometry.Rectangle(bach.geometry.Point(1, 1), 1, 1)
result = rectangle_one.overlap(rectangle_one)
assert(result is True), "Expected: True - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1, 1), 2, 2)
result = rectangle_one.overlap(rectangle_two)
assert(result is True), "Expected: True - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(2, 2), 1, 1)
result = rectangle_one.overlap(rectangle_two)
assert(result is True), "Expected: True - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(2.1, 2.1), 1, 1)
result = rectangle_one.overlap(rectangle_two)
assert(result is False), "Expected: False - Computed: {}".format(result)
rectangle_one = bach.geometry.Rectangle(bach.geometry.Point(2, 2), 1, 1)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(3, 3), 2.5, 2.5)
result = rectangle_one.overlap(rectangle_two)
assert(result is True), "Expected: True - Computed: {}".format(result)

rectangle_one = bach.geometry.Rectangle(bach.geometry.Point(1, 1), 1, 1)
result = rectangle_one.overlap_area(rectangle_one)
assert(result == 1), "Expected: 1 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1, 1), 0.5, 0.5)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.25)), "Expected: 0.25 - Computed: {}".format(result)
result = rectangle_two.overlap_area(rectangle_one)
assert(math.isclose(result, 0.25)), "Expected: 0.25 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(2, 2), 0.5, 0.5)
result = rectangle_one.overlap_area(rectangle_two)
assert(result == 0), "Expected: 0 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(2, 2), 1, 1)
result = rectangle_one.overlap_area(rectangle_two)
assert(result == 0), "Expected: 0 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(2, 2), 1.1, 1.1)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.0025)), "Expected: 0.0025 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1.5, 1), 1, 1)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.5)), "Expected: 0.5 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(0.5, 0.5), 1, 1)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.25)), "Expected: 0.25 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1, 2), 1, 1)
result = rectangle_one.overlap_area(rectangle_two)
assert(result == 0), "Expected: 0 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1.5, 0.75), 1, 0.5)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.25)), "Expected: 0.25 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1.5, 1), 0.5, 0.5)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.125)), "Expected: 0.125 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1, 2), 0.5, 2.5)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.375)), "Expected: 0.375 - Computed: {}".format(result)
rectangle_two = bach.geometry.Rectangle(bach.geometry.Point(1.5, 1.5), 1.9, 1.9)
result = rectangle_one.overlap_area(rectangle_two)
assert(math.isclose(result, 0.9025)), "Expected: 0.9025 - Computed: {}".format(result)
