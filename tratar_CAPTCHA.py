import cv2
import os
import glob
from PIL import Image


# Vai ver a pasta de origem e a pasta de destino
def tratar_img(pasta_origem, pasta_destino="ajeitado"):
    
    arquivos = glob.glob(f"{pasta_origem}/*")
    
    for arquivo in arquivos:
        
        img = cv2.imread(arquivo)

        img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        _, tratada = cv2.threshold(img_cinza, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
        
        nome = os.path.basename(arquivo)
        
        cv2.imwrite(f"{pasta_destino}/{nome}", tratada)
        
        img = Image.open("2/imagem_tratada_3.png")
        
    arquivos = glob.glob(f"{pasta_destino}/*")
    
    for arquivo in arquivos:
        
        img = Image.open(arquivo)
        
        img = img.convert("P")
        
        img2 = Image.new("P", img.size, color = (255, 255, 255))
        
        black = (0, 0, 0)

        for x in range(img.size[1]):  # 1 = colunas da imagem
            for y in range(img.size[0]):  # 0 = linhas da imagem
                cor = img.getpixel((y, x))
                if cor < 115:
                    img2.putpixel((y, x), black)
        nome = os.path.basename(arquivo)
        img2.save(f"{pasta_destino}/{nome}")


if __name__ == "__main__":
    tratar_img("bdcaptcha")
