from ipey.document import Document
from ipey.primitive import Rectangle, Line
from ipey.helper import convertColor

document = Document()
page = document.createPage()

line = Line([(200,200),(300,300),(500,500)])
page.add(line)

rect = Rectangle((300,400),200,200)
rect.fill = convertColor('#fafa6e')
rect.layer = 'rectangles'
page.add(rect)

rect2 = rect.clone()
rect2.translate(200,200)
rect2.layer = 'rectangles2'
page.add(rect2)

page.createView('view1', 'rectangles2')
page.createView('view2', ['rectangles', 'rectangles2', 'test'])


document.write('examples/output/layerTest.xml')
