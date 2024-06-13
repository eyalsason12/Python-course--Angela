import colorgram
rgb_colors = []
colors = colorgram.extract('image.jpg', 40)
for color in colors:
    rgb = color.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)