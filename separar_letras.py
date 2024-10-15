import cv2 as cv
import os
import glob

arquivos = glob.glob("ajeitado/*")
for arquivo in arquivos:
    imagem = cv.imread(arquivo)
    imagem = cv.cvtColor(imagem, cv.COLOR_RGB2GRAY)

    _, nova_imagem = cv.threshold(imagem, 0, 255, cv.THRESH_BINARY_INV)

    # Encontrar os contornos de cada letra
    contornos, _ = cv.findContours(
        nova_imagem, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    regiao_letra = []
    # Filtrar os contornos que são de letras
    for contorno in contornos:
        (x, y, largura, altura) = cv.boundingRect(contorno)
        area = cv.contourArea(contorno)
        if area > 115:
            regiao_letra.append((x, y, largura, altura))

    if len(regiao_letra) != 5:
        continue

    imagem_final = cv.merge([imagem]*3)
    i = 0
    for retangulo in regiao_letra:
        x, y, largura, altura = retangulo
        imagem_letra = imagem[y-2:y+altura+2, x-2:x+largura+2]
        i += 1
        nome_arquivo = os.path.basename(arquivo).replace(f".png", f"letra{i}.png")
        cv.imwrite(f"letras/{nome_arquivo}", imagem_letra)
        cv.rectangle(imagem_final, (x-2, y-2), (x+largura+2, y+altura+2), (0,255,0))
    nome_arquivo = os.path.basename(arquivo)
    cv.imwrite(f"identificado/{nome_arquivo}", imagem_final)