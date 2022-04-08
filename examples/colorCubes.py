from ipey.document import Document
from ipey.primitive import Rectangle
from ipey.helper import convertColor

colors = ['#fafa6e','#edf76f','#e0f470','#d4f171','#c8ed73','#bcea75','#b0e678','#a5e27a','#99de7c','#8eda7f','#83d681','#79d283','#6ecd85','#64c987','#5ac489','#50bf8b','#46bb8c','#3cb68d','#32b18e','#28ac8f','#1ea78f','#12a28f','#039d8f','#00988e','#00938d','#008e8c','#00898a','#008488','#007e86','#007983','#057480','#0e6f7d','#156a79','#1a6575','#1e6071','#225b6c','#255667','#275163','#294d5d','#2a4858']

document = Document()
document.crop = True
page = document.createPage()

width = 400
height = 400

prototype = Rectangle((410,410), width, height)
prototype.stroke = None
margin = 20

for i in range(8):
    for j in range(5):
        rect = prototype.clone()
        color = convertColor(colors[i * 5 + j])
        rect.fill = color[1]
        rect.translate(j * margin + j * width, i * margin + i * height)
        page.add(rect)

document.write('examples/output/color_cubes.xml')
