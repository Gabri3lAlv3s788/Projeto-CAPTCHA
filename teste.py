import cv2 as cv

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
    