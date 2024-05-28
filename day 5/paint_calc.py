def paint_calc(height, width, cover):
    number_of_cans = int((height * width) / cover) + ((height * width) % cover > 0)
    print(f"you'll need {number_of_cans} cans of paint")

test_h = int(input("what is the height of the wall? "))
test_w = int(input("what is the width of the wall? "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
