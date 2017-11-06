from PIL import Image
import SimpleNet as net

def t():
    pic = []
    im = Image.open("test.png") 
    pix = im.load()
    
    for y in range(28):
        for x in range(28):
            pic.append(pix[x, y][0] / 255)
    net.test(pic)

pic = []
data = []
answer = []

X = ["x0.png", "x1.png", "x2.png", "x3.png", "x4.png", "x5.png", "x6.png", "x7.png", "x8.png", "x9.png", "x10.png", "x11.png", "x12.png", "x13.png", "x14.png", ]
O = ["o0.png", "o1.png", "o2.png", "o3.png", "o4.png", "o5.png", "o6.png", "o7.png", "o8.png", "o9.png", "o10.png", "o11.png", "o12.png", "o13.png", "o14.png", ]

for fname in X:
    im = Image.open("TrainingImages/" + fname) 
    pix = im.load()

    for y in range(28):
        for x in range(28):
            pic.append(pix[x, y][0] / 255)
        
    data.append(pic)
    answer.append(1)
    pic = []
    
for fname in O:
    im = Image.open("TrainingImages/" + fname) 
    pix = im.load()

    for y in range(28):
        for x in range(28):
            pic.append(pix[x, y][0] / 255)
        
    data.append(pic)
    answer.append(0)
    pic = []

net.data = data
net.answer = answer
net.train(20000, 1)