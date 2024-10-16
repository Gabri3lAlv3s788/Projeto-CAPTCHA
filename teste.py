import cv2
from PIL import Image

metodo = [

    cv2.THRESH_BINARY,
    cv2.THRESH_BINARY_INV,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TOZERO_INV,

]

img = cv2.imread("1/telanova0.png")

img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

i = 0

for metodos in metodo:

    i += 1
    _, tratada = cv2.threshold(img_cinza, 127, 255, metodos or cv2.THRESH_OTSU)
    cv2.imwrite(f"2/imagem_tratada_{i}.png", tratada)


img = Image.open("2/imagem_tratada_3.png")
img = img.convert("P")
img2 = Image.new("P", img.size, color = (255, 255, 255))
black = (0, 0, 0)

for x in range(img.size[1]):  # 1 = colunas da imagem
    for y in range(img.size[0]):  # 0 = linhas da imagem
        cor = img.getpixel((y, x))
        if cor < 115:
            img2.putpixel((y, x), black)

img2.save("2/img_final.png")
