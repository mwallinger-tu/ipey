from ipey.document import Document
from ipey.primitive import Label, Minipage
from ipey.helper import convertColor

colors = ['#fafa6e','#edf76f','#e0f470','#d4f171','#c8ed73','#bcea75','#b0e678','#a5e27a','#99de7c','#8eda7f','#83d681','#79d283','#6ecd85','#64c987','#5ac489','#50bf8b','#46bb8c','#3cb68d','#32b18e','#28ac8f','#1ea78f','#12a28f','#039d8f','#00988e','#00938d','#008e8c','#00898a','#008488','#007e86','#007983','#057480','#0e6f7d','#156a79','#1a6575','#1e6071','#225b6c','#255667','#275163','#294d5d','#2a4858']

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

document.write('src/examples/output/labels.xml')
