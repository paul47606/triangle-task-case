x = float(input('Enter your X value: '))
y = float(input('Enter your Y value: '))

# A = (x1,y1) = (-10,0)
x1 = -10
y1 = 0

# B = (x2,y2) = (0,10)
x2 = 0
y2 = 10

# C = (x3,y3) = (10,0)
x3 = 10
y3 = 0

# area of triangle formula:
area_of_traingle = abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))

# The areas of the subtriangles are calculated using -
#   the same formula but with one of the vertices replaced by the point (x,y)

area_of_subtraingle_1 = abs((x1-x)*(y2-y) - (x2-x)*(y1-y))
area_of_subtraingle_2 = abs((x2-x)*(y3-y) - (x3-x)*(y2-y))
area_of_subtraingle_3 = abs((x3-x)*(y1-y) - (x1-x)*(y3-y))

# to know where the vertex lies on

if area_of_traingle == area_of_subtraingle_1 + area_of_subtraingle_2 + area_of_subtraingle_3:
    print(f"congrats.., the points {x,y} lies on the triangle")
else:
    print(f"The vertex {x,y} lies outside of the triangle.")

