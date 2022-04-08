from ipey.document import Document
from ipey.primitive import Label, Minipage
from ipey.helper import convertColor


document = Document()
page = document.createPage()

label = Label('test', (200, 300))
page.add(label)

label = Label('math', (400, 300))
label.isMath = True
page.add(label)

label = Label('long red text in center', (400, 500))
label.vAlign = 'center'
label.hAlign = 'center'
label.stroke = 'red'
label.size = 'LARGE'
page.add(label)

minipage = Minipage('this is a very long text that should be displayed as a minipage with automatic line breaks depending on the width', (100, 700))
minipage.width = 200
page.add(minipage)

document.write('examples/output/labels.xml')
