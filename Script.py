import pyautogui as p
import mss
from PIL import Image
p.moveTo(230,222)
p.click()
i = 0
j = 160
while i < 10000:
    with mss.mss() as sct:
        region = {'top': 178, 'left': 108, 'width': 300, 'height': 100}
        img = sct.grab(region)   
        mss.tools.to_png(img.rgb, img.size, output='dummy.png')
    im = Image.open('dummy.png','r')
    (x,y,z) = im.getpixel((j,48))
    (x1,y1,z1) = im.getpixel((j,63))
    (x2,y2,z2) = im.getpixel((j,35))
    if x1 == 0 | x1 == 172:
        p.typewrite(['up','up','up','up','up'])
        print('1')
        print(im.getpixel((j,50)))
    elif x == 0 | x == 172:
        p.typewrite(['up','up','up','up','up'])
        print('2')
        print(im.getpixel((j,63)))
    elif x2 == 0 | x2 == 172:
        p.typewrite(['up','up','up','up','up'])
        print('3')
        print(im.getpixel((j,35)))
    else : 
        print('\t', end = '')
        print(im.getpixel((j,50))) 
        print('\t', end = '')
        print(im.getpixel((j,63))) 
        print('\t', end = '')
        print(im.getpixel((j,35)))       
    (x3,y3,z3) = im.getpixel((226,14))
    (x4,y4,z4) = im.getpixel((241,14))
    if x3 == x4 == 172:
        i = 10001
        print('stop')
    i = i + 1
    if i%200 == 0:
        j = j + 1
        print(j)
