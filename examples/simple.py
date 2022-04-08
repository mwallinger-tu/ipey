from typing import Tuple
from ipey.document import Document
from ipey.primitive import Rectangle, Line, Circle, Arc, Glyph
from ipey.helper import convertColor
from ipey.primitive import RectangleC
from ipey.primitive.ellipse import Ellipse

colors = ['#fafa6e','#edf76f','#e0f470','#d4f171','#c8ed73','#bcea75','#b0e678','#a5e27a','#99de7c','#8eda7f','#83d681','#79d283','#6ecd85','#64c987','#5ac489','#50bf8b','#46bb8c','#3cb68d','#32b18e','#28ac8f','#1ea78f','#12a28f','#039d8f','#00988e','#00938d','#008e8c','#00898a','#008488','#007e86','#007983','#057480','#0e6f7d','#156a79','#1a6575','#1e6071','#225b6c','#255667','#275163','#294d5d','#2a4858']

document = Document(styles=["kit-colors.isy"])
document.crop = True
page = document.createPage()

# line1 = Line([(0,0), (100,100), (0,100)])
# page.add(line1)

# line = line1.clone()
# line.translate(150,0)
# page.add(line)

# line = line.clone()
# line.translate(150,150)
# line.rotate(3.1415)
# page.add(line)

# line = line.clone()
# line.rotate(3.1415, line.points[0])
# page.add(line)

# circle = Circle((400,400), 20)
# page.add(circle)

# arc = Arc((300,300), (400,400), (500, 300))
# page.add(arc)


# arc = Arc((500,500), (500,600), (600, 600))
# page.add(arc)

# arc = Arc((600,600), (700,600), (700, 500))
# page.add(arc)

# arc = Arc((700,500), (700,400), (600, 400))
# page.add(arc)

# arc = Arc((600,400), (500,400), (500, 500))
# page.add(arc)


# arc = Arc((200,600), (100,600), (100, 500))
# page.add(arc)

# arc = Arc((300,500), (300,600), (200, 600))
# page.add(arc)

# arc = Arc((200,400), (300,400), (300, 500))
# page.add(arc)

arc = Arc((600,500), (700,900), (200, 900))
arc.stroke = 'KITlilac'
arc.arrow = True
page.add(arc)

#glyph = Glyph((700,900))
#page.add(glyph)

arc = Arc((100,500), (155,455), (200, 400))
arc.arrow = True
page.add(arc)

# rectC = RectangleC((80,80), 100, 50)
# page.add(rectC)

# ell = Ellipse((500,200), (500,300), (500,200))
# ell.stroke = 'blue'
# page.add(ell)

document.write('src/examples/output/simple.xml')
