from ipey.document import Document
from ipey.primitive import Glyph, Line, Polygon
from ipey.helper import convertColor

import random


points = [(random.randint(0,500),random.randint(0,500)) for i in range(40)]
#points = [(100,100), (300,100), (300, 300), (100,300)]

document = Document()
document.crop = True

pagePoints = document.createPage()

for p in points:
    glyph = Glyph(p, 'mark/fdisk(sfx)')
    glyph.fill = convertColor('#000000')[1]
    glyph.stroke = convertColor('#ffffff')[1]
    glyph.pen = 'fat'

    pagePoints.add(glyph)


def get_slope(p1, p2):
    if p1[0] == p2[0]:
        return float('inf')
    else:
        return 1.0*(p1[1]-p2[1])/(p1[0]-p2[0])

def get_cross_product(p1,p2,p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))


points.sort(key=lambda x:[x[0],x[1]])
start = points.pop(0)

hull = [start]

points.sort(key=lambda p: (get_slope(p,start), -p[1],p[0]))

for p in points:
    hull.append(p)
    while len(hull) > 2 and get_cross_product(hull[-3],hull[-2],hull[-1]) < 0:
        hull.pop(-2)

    page = document.copyPage(pagePoints)
    line = Line(hull)
    page.add(line)
    line.stroke = 'green'

page = document.copyPage(pagePoints)
poly = Polygon(hull)
page.add(poly)

document.write('examples/output/convexHull.xml')