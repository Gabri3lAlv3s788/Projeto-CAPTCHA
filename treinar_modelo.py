import cv2
import os
import numpy as np
import pickle
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
import keras as ks
from helpers import resize_to_fit

dados = []
rotulos = []
pasta_base_img = "base"

imagens = paths.list_images(pasta_base_img)

for arquivo in imagens:
    rotulo = arquivo.split(os.path.sep)[-2]
    imagem = cv2.imread(arquivo)
    imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Padronizar a imagem em 20x20
    
    imagem = resize_to_fit(imagem, 20, 20)
    
    # Adicionar uma dimensão na imagem para o keras poder ler
    
    imagem = np.expand_dims(imagem, axis=2)
    
    rotulos.append(rotulo)
    dados.append(imagem)
    
dados = np.array(dados, dtype="float") / 255

rotulos = np.array(rotulos)

# Separação em dados de treino e teste 75 / 25

(X_train, X_test, Y_train, Y_test) = train_test_split(dados, rotulos, test_size=0.25, random_state=0)

lb = LabelBinarizer().fit(Y_train)
Y_train = lb.transform(Y_train)
Y_test = lb.transform(Y_test)

with open("rotulos_modelo.dat", "wb") as arquivo_pickle:
    pickle.dump(lb, arquivo_pickle)

# Criar e treinar a IA

modelo = ks.models.Sequential()

modelo.add(ks.layers.Conv2D(20, (5, 5,), padding="same", input_shape=(20, 20, 1), activation="relu"))
modelo.add(ks.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

modelo.add(ks.layers.Conv2D(50, (5, 5), padding="same", activation="relu"))
modelo.add(ks.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

modelo.add(ks.layers.Flatten())
modelo.add(ks.layers.Dense(500, activation="relu"))

# Camada de saída

modelo.add(ks.layers.Dense(26, activation="softmax"))

# Compilar as camadas

modelo.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

modelo.fit(X_train, Y_train, validation_data=(X_test, Y_test), batch_size=26, epochs=10, verbose=1)

# Salvar o modelo em um arquivo

modelo.save("modelo_treinado.hdf5")
