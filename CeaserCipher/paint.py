from math import ceil # this way of writing only imports the ceil method from math library and saves space and time
                       # Also, a method imported as such does not to be written as math.ceil but just as ceil

def cover_wall(width, height):
    area = width * height
    coverage = 5
    # number_of_paint_cans = round(area / coverage)
    number_of_paint_cans = ceil(area / coverage) # the number needs to be rounded to it's ceil value
    if number_of_paint_cans == 1:
        print("1 paint can is needed to paint the wall")
    else:
        print(f"{number_of_paint_cans} paint cans are needed to paint the wall")

cover_wall(9,4)
