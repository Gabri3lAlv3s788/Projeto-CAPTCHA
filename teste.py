import cv2 as cv
from PIL import Image

metodo = [
    
    cv.THRESH_BINARY,
    cv.THRESH_BINARY_INV,
    cv.THRESH_TRUNC, 
    cv.THRESH_TOZERO,
    cv.THRESH_TOZERO_INV,
 
]

img = cv.imread("1/telanova0.png")

img_cinza = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

i = 0

for metodos in metodo:
    
    i += 1
    _, tratada = cv.threshold(img_cinza, 127, 255, metodos or cv.THRESH_OTSU)
    cv.imwrite(f"2/imagem_tratada_{i}.png", tratada)
    

img = Image.open("2/imagem_tratada_3.png")
img = img.convert("P")
img2 = Image.new ("P", img.size, color = (255, 255, 255))
black = (0, 0, 0)

for x in range(img.size[1]): # 1 = colunas da imagem
    for y in range(img.size[0]): # 0 = linhas da imagem
        cor = img.getpixel((y, x))
        if cor < 115: 
            img2.putpixel((y, x), black)
            print("AQUI")
        
img2.save('2/img_final.png')