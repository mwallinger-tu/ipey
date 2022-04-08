from ipey.document import Document, Margin
from ipey.primitive import Polygon
from ipey.helper import convertColor

colors = ['#fafa6e','#edf76f','#e0f470','#d4f171','#c8ed73','#bcea75','#b0e678','#a5e27a','#99de7c','#8eda7f','#83d681','#79d283','#6ecd85','#64c987','#5ac489','#50bf8b','#46bb8c','#3cb68d','#32b18e','#28ac8f','#1ea78f','#12a28f','#039d8f','#00988e','#00938d','#008e8c','#00898a','#008488','#007e86','#007983','#057480','#0e6f7d','#156a79','#1a6575','#1e6071','#225b6c','#255667','#275163','#294d5d','#2a4858']

colors.reverse()
n = len(colors)
factor = 0.92
factory = 0.8

document = Document()
document.crop = True
document.margin = Margin(top=0, bottom=0, left=0, right=0)
page = document.createPage()

rect = Polygon([(0,0), (0, 600), (600,600), (600,0)])
rect.pen = 2.0
rect.stroke = colors[0]
rect.fill = colors[0]
page.add(rect)

for i in range(1,n):
    rect = rect.clone()
    rect.stroke = colors[i]
    rect.fill = colors[i]
    points = rect.points
    newP = []

    for j in range(4):
        p1 = points[j]
        p2 = points[(j + 1) % 4]

        dx = p2[0] - p1[0]
        dy = p2[1] - p2[0]

        pNew = (p1[0] + dx * factor, p1[1] + dy * factor)
        newP.append(pNew)

    rect.points = newP
    page.add(rect)


document.write('examples/output/spiral.xml')
